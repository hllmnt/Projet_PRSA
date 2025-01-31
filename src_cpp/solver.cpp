#include "../headers/solver.h"

Solver::Solver(arma::cx_mat _psi, arma::cx_mat V, double dx, double dy, double dt, double m ){
    psi = _psi;
    extendedPsi = arma::cx_mat(_psi.n_rows + 2, _psi.n_cols + 2, arma::fill::zeros);

    i_dt_over_hb_times_V_plus_i_dt_hb_over_m_ddx_plus_i_dt_hb_over_m_ddy = -(arma::cx_double(0, dt / hb) * V
        + arma::cx_double(0, dt * hb / (m * dx * dx)) + arma::cx_double(0, dt * hb / (m * dy * dy)));

    i_dt_hb_over_2m_ddx = arma::cx_double(0, dt * hb / (2 * m * dx * dx));
    i_dt_hb_over_2m_ddy = arma::cx_double(0, dt * hb / (2 * m * dy * dy));
}

void Solver::updateShiftedPsis (const arma::cx_mat& _psi) {
// Update extendedPsi which is useful for generating the submatrices below
    extendedPsi.submat(1, 1, _psi.n_rows, _psi.n_cols) = _psi;

// Generate matrices to vectorize the calculation of psi
    psi_x_plus_dx = extendedPsi.submat(2, 1, extendedPsi.n_rows-1, extendedPsi.n_cols-2);
    psi_x_minus_dx = extendedPsi.submat(0, 1, extendedPsi.n_rows-3, extendedPsi.n_cols-2);
    psi_y_plus_dy = extendedPsi.submat(1, 2, extendedPsi.n_rows-2, extendedPsi.n_cols-1);
    psi_y_minus_dy = extendedPsi.submat(1, 0, extendedPsi.n_rows-2, extendedPsi.n_cols-3);
}

void Solver::generateNextStep_FTCS () {
    updateShiftedPsis(psi);
    psi += i_dt_over_hb_times_V_plus_i_dt_hb_over_m_ddx_plus_i_dt_hb_over_m_ddy % psi
            + i_dt_hb_over_2m_ddx * (psi_x_plus_dx + psi_x_minus_dx)
            + i_dt_hb_over_2m_ddy * (psi_y_plus_dy + psi_y_minus_dy);
}

void Solver::generateNextStep_BTCS () {
    newGuessedPsi = psi;

    double epsilon = 1.0e-14;

    do {
        lastGuessedPsi = newGuessedPsi;
        updateShiftedPsis(lastGuessedPsi);
        newGuessedPsi = psi + i_dt_over_hb_times_V_plus_i_dt_hb_over_m_ddx_plus_i_dt_hb_over_m_ddy % lastGuessedPsi
                            + i_dt_hb_over_2m_ddx * (psi_x_plus_dx + psi_x_minus_dx)
                            + i_dt_hb_over_2m_ddy * (psi_y_plus_dy + psi_y_minus_dy);
    } 
    while (arma::norm(newGuessedPsi - lastGuessedPsi) > epsilon);

    psi = newGuessedPsi;
};

void Solver::generateNextStep_CTCS () {
    updateShiftedPsis(psi);
    arma::cx_mat preCalculatedPsiPart = psi + 0.5*(i_dt_over_hb_times_V_plus_i_dt_hb_over_m_ddx_plus_i_dt_hb_over_m_ddy % psi
                                                    + i_dt_hb_over_2m_ddx * (psi_x_plus_dx + psi_x_minus_dx)
                                                    + i_dt_hb_over_2m_ddy * (psi_y_plus_dy + psi_y_minus_dy));
    newGuessedPsi = psi;

    double epsilon = 1.0e-14;
    
    do {
        lastGuessedPsi = newGuessedPsi;
        updateShiftedPsis(lastGuessedPsi);
        newGuessedPsi = preCalculatedPsiPart + 0.5*(i_dt_over_hb_times_V_plus_i_dt_hb_over_m_ddx_plus_i_dt_hb_over_m_ddy % lastGuessedPsi
                                                    + i_dt_hb_over_2m_ddx * (psi_x_plus_dx + psi_x_minus_dx)
                                                    + i_dt_hb_over_2m_ddy * (psi_y_plus_dy + psi_y_minus_dy));
    } 
    while (arma::norm(newGuessedPsi - lastGuessedPsi) > epsilon);

    psi = newGuessedPsi;
};
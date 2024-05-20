#include "../headers/solver.h"

Solver::Solver(arma::cx_mat _psi, arma::cx_mat V, double dx, double dy, double dt, double m ){
    psi = _psi;
    
    extendedPsi = arma::cx_mat(_psi.n_rows + 2, _psi.n_cols + 2, arma::fill::zeros);
    extendedPsi(arma::span(1, _psi.n_rows), arma::span(1, _psi.n_cols)) = _psi;

    i_dt_over_hb_times_V_plus_i_dt_hb_over_m_ddx_plus_i_dt_hb_over_m_ddy = -(arma::cx_double(0, dt / Constants::hb) * V
        + arma::cx_double(0, dt * Constants::hb / (m * dx * dx)) + arma::cx_double(0, dt * Constants::hb / (m * dy * dy)));
    i_dt_hb_over_2m_ddx = arma::cx_double(0, dt * Constants::hb / (2 * m * dx * dx));
    i_dt_hb_over_2m_ddy = arma::cx_double(0, dt * Constants::hb / (2 * m * dy * dy));
}

void Solver::generateNextStep_FTCS () {
// Generate matrices to vectorize the calculation of the next psi
    arma::cx_mat psi_x_plus_dx = extendedPsi.submat(2, 1, extendedPsi.n_rows-1, extendedPsi.n_cols-2);
    arma::cx_mat psi_x_minus_dx = extendedPsi.submat(0, 1, extendedPsi.n_rows-3, extendedPsi.n_cols-2);

    arma::cx_mat psi_y_plus_dy = extendedPsi.submat(1, 2, extendedPsi.n_rows-2, extendedPsi.n_cols-1);
    arma::cx_mat psi_y_minus_dy = extendedPsi.submat(1, 0, extendedPsi.n_rows-2, extendedPsi.n_cols-3);

    psi += i_dt_over_hb_times_V_plus_i_dt_hb_over_m_ddx_plus_i_dt_hb_over_m_ddy % psi
                    + i_dt_hb_over_2m_ddx * (psi_x_plus_dx + psi_x_minus_dx)
                    + i_dt_hb_over_2m_ddy * (psi_y_plus_dy + psi_y_minus_dy);

    extendedPsi(arma::span(1, psi.n_rows), arma::span(1, psi.n_cols)) = psi;
}

void Solver::generateNextStep_BTCS () {
    // TO DO
};

void Solver::generateNextStep_CTCS () {
    // TO DO
};
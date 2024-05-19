#include "../headers/solver.h"

Solver::Solver(arma::cx_mat _psi, arma::cx_mat V, double dx, double dy, double dt, double m ){
    psi = _psi;

    i_dt_over_hb_times_V_plus_i_dt_hb_over_m_ddx_plus_i_dt_hb_over_m_ddy = -(arma::cx_double(0, dt / Constants::hb) * V
        + arma::cx_double(0, dt * Constants::hb / (m * dx * dx)) + arma::cx_double(0, dt * Constants::hb / (m * dy * dy)));
    i_dt_hb_over_2m_ddx = arma::cx_double(0, dt * Constants::hb / (2 * m * dx * dx));
    i_dt_hb_over_2m_ddy = arma::cx_double(0, dt * Constants::hb / (2 * m * dy * dy));

    arma::rowvec row_zeros = arma::rowvec(_psi.n_cols,arma::fill::zeros);
    cx_row_zeros = arma::cx_rowvec(row_zeros,row_zeros);
    arma::colvec col_zeros = arma::colvec(_psi.n_rows,arma::fill::zeros);
    cx_col_zeros = arma::cx_colvec(col_zeros,col_zeros);
}

void Solver::generateNextStep_FTCS () {
// Generate matrices to vectorize the calculation of the next psi
    arma::cx_mat psi_x_plus_dx = psi.submat(1, 0, psi.n_rows-1, psi.n_cols-1);
    psi_x_plus_dx.insert_rows(psi_x_plus_dx.n_rows, cx_row_zeros);

    arma::cx_mat psi_x_minus_dx = psi.submat(0, 0, psi.n_rows-2, psi.n_cols-1);
    psi_x_minus_dx.insert_rows(0, cx_row_zeros);

    arma::cx_mat psi_y_plus_dy = psi.submat(0, 1, psi.n_rows-1, psi.n_cols-1);
    psi_y_plus_dy.insert_cols(psi_y_plus_dy.n_cols, cx_col_zeros);

    arma::cx_mat psi_y_minus_dy = psi.submat(0, 0, psi.n_rows-1, psi.n_cols-2);
    psi_y_minus_dy.insert_cols(0, cx_col_zeros);

    psi += i_dt_over_hb_times_V_plus_i_dt_hb_over_m_ddx_plus_i_dt_hb_over_m_ddy % psi
            + i_dt_hb_over_2m_ddx * (psi_x_plus_dx + psi_x_minus_dx)
            + i_dt_hb_over_2m_ddy * (psi_y_plus_dy + psi_y_minus_dy);
}

void Solver::generateNextStep_BTCS () {
    // TO DO
};

void Solver::generateNextStep_CTCS () {
    // TO DO
};
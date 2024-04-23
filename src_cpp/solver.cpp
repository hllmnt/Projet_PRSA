#include "../headers/solver.h"

Solver::Solver(arma::mat psi_real, arma::mat psi_imaginary, arma::mat V_real, arma::mat V_imaginary, double grid_interval, double dt, double m) {
    psi = arma::cx_mat(psi_real,psi_imaginary);
    V = arma::cx_mat(V_real,V_imaginary);
    dx = grid_interval;
    dy = grid_interval;
    dt = dt;
    m = m;

    i_dt_over_hb = arma::cx_double(0, dt / Constantes::hb);
    i_dt_hb_over_m_ddx_plus_i_dt_hb_over_m_ddy = arma::cx_double(0, dt * Constantes::hb / (m * dx * dx)) + arma::cx_double(0, dt * Constantes::hb / (m * dy * dy));
    i_dt_hb_over_2m_ddx = arma::cx_double(0, dt * Constantes::hb / (2 * m * dx * dx));
    i_dt_hb_over_2m_ddy = arma::cx_double(0, dt * Constantes::hb / (2 * m * dy * dy));
}

void Solver::generateNextStep_FTCS () {
    arma::colvec col_zeros = arma::colvec(psi.n_rows,arma::fill::zeros);
    arma::cx_colvec cx_col_zeros = arma::cx_colvec(col_zeros,col_zeros);

    arma::cx_mat psi_x_plus_dx = psi.submat(0,1,-1,-1);
    psi_x_plus_dx.insert_cols(-1,cx_col_zeros);

    arma::cx_mat psi_x_minus_dx = psi.submat(0,0,-2,-1);
    psi_x_minus_dx.insert_cols(0,cx_col_zeros);

    arma::rowvec row_zeros = arma::rowvec(psi.n_rows,arma::fill::zeros);
    arma::cx_rowvec cx_row_zeros = arma::cx_rowvec(row_zeros,row_zeros);

    arma::cx_mat psi_y_plus_dy = psi.submat(0,1,-1,-1);
    psi_y_plus_dy.insert_rows(-1,cx_row_zeros);

    arma::cx_mat psi_y_minus_dy = psi.submat(0,0,-1,-2);
    psi_y_minus_dy.insert_rows(0,cx_row_zeros);

    psi += -(i_dt_over_hb * V + i_dt_hb_over_m_ddx_plus_i_dt_hb_over_m_ddy) * psi
            + i_dt_hb_over_2m_ddx * (psi_x_plus_dx + psi_x_minus_dx)
            + i_dt_hb_over_2m_ddy * (psi_y_plus_dy + psi_y_minus_dy);
}

void Solver::generateNextStep_BTCS () {
    // TO DO
};

void Solver::generateNextStep_CTCS () {
    // TO DO
};
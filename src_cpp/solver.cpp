#include "../headers/solver.h"

Solver::Solver(arma::cx_mat psi, arma::cx_mat V, double grid_interval, double dt, double m)
    : psi(psi), V(V), dt(dt), m(m) {
    dx = grid_interval;
    dy = grid_interval;
    i_dt_over_hb = arma::cx_double(0, dt / Constantes::hb);
    i_dt_hb_over_m_ddx_plus_i_dt_hb_over_m_ddy = arma::cx_double(0, dt * Constantes::hb / (m * dx * dx)) + arma::cx_double(0, dt * Constantes::hb / (m * dy * dy));
    i_dt_hb_over_2m_ddx = arma::cx_double(0, dt * Constantes::hb / (2 * m * dx * dx));
    i_dt_hb_over_2m_ddy = arma::cx_double(0, dt * Constantes::hb / (2 * m * dy * dy));
}

arma::cx_mat getPsi () {
    return psi;
}

void Solver::generateNextStep_FTCS () {
    arma::cx_mat psi_x_plus_dx = arma::shift(psi,-1,0); // arma::sub_mat is maybe better
    psi_x_plus_dx.row(-1).zeros(); // the psi function is null when outside the matrix

    arma::cx_mat psi_x_minus_dx = arma::shift(psi,1,0);
    psi_x_minus_dx.row(0).zeros();

    arma::cx_mat psi_y_plus_dy = arma::shift(psi,-1,1);
    psi_y_plus_dy.col(-1).zeros();

    arma::cx_mat psi_y_minus_dy = arma::shift(psi,1,1);
    psi_y_minus_dy.col(0).zeros();


    arma::cx_mat psi_x_plus_dx = psi.submat(0, 1, psi.n_rows-1, psi.n_cols-1);
    psi_x_plus_dx.insert_cols(-1,fill::zeroes);

    arma::cx_mat psi_x_minus_dx = psi.submat(0, 0, psi.n_rows-2, psi.n_cols-1);
    psi_x_minus_dx.insert_cols(0).zeros();

    arma::cx_mat psi_y_plus_dy = psi.submat(0, 1, psi.n_rows-1, psi.n_cols-1);
    psi_y_plus_dy.insert_rows(psi.n_cols - 1).zeros();

    arma::cx_mat psi_y_minus_dy = psi.submat(0, 0, psi.n_rows-1, psi.n_cols-2);
    psi_y_minus_dy.insert_rows(0).zeros();


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
#include "../headers/solver.h"

Solver::Solver(PreComputed* preComputed, arma::cx_mat psi, arma::cx_mat V, unsigned int nbXPts, 
                unsigned int nbYPts, double dx, double dy, double dt, double mass)
            : preComputed(preComputed), psi(psi), V(V), nbXPts(nbXPts), nbYPts(nbYPts), dx(dx), dy(dy), dt(dt), mass(mass) {}

arma::cx_mat getPsi () {
    return psi;
}

void Solver::generateNextStep_FTCS () {
    arma::cx_mat psi_x_plus_dx = shift (psi,-1,0);
    psi_x_plus_dx.row(-1).zeros(); // the psi function is null when outside the matrix

    arma::cx_mat psi_x_minus_dx = shift (psi,1,0);
    psi_x_minus_dx.row(0).zeros();

    arma::cx_mat psi_y_plus_dy = shift (psi,-1,1);
    psi_y_plus_dy.col(-1).zeros();

    arma::cx_mat psi_y_minus_dy = shift (psi,1,1);
    psi_y_minus_dy.col(0).zeros();

    psi += -(preComputed->i_dt_over_hb * V + preComputed->i_dt_hb_over_m_ddx_plus_i_dt_hb_over_m_ddy) * psi
            + preComputed->i_dt_hb_over_2m_ddx * (psi_x_plus_dx + psi_x_minus_dx)
            + preComputed->i_dt_hb_over_2m_ddy * (psi_y_plus_dy + psi_y_minus_dy);
}

void Solver::generateNextStep_BTCS () {
    // TO DO
};

void Solver::generateNextStep_CTCS () {
    // TO DO
};
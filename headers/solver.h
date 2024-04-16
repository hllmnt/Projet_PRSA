#ifndef SOLVER_H
#define SOLVER_H
#include <armadillo>
#include "constantes.h"

class Solver {
private:
    const arma::cx_mat V;
    const double grid_interval;
    const double dt;
    const double m;

    const arma::cx_double i_dt_over_hb;
    const arma::cx_double i_dt_hb_over_m_ddx_plus_i_dt_hb_over_m_ddy;
    const arma::cx_double i_dt_hb_over_2m_ddx;
    const arma::cx_double i_dt_hb_over_2m_ddy;

public:
    arma::cx_mat psi;

    Solver(arma::cx_mat,arma::cx_mat,double,double,double);

    arma::cx_mat getPsi ();

// return the following state of the wave function
    void generateNextStep_FTCS ();
    void generateNextStep_BTCS ();
    void generateNextStep_CTCS ();
};

#endif // SOLVER_H
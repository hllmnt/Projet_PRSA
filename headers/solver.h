#ifndef SOLVER_H
#define SOLVER_H
#include <armadillo>
#include "constantes.h"

class Solver {
private:
    arma::cx_mat V;
    double dx;
    double dy;
    double dt;
    double m;

    arma::cx_double i_dt_over_hb;
    arma::cx_double i_dt_hb_over_m_ddx_plus_i_dt_hb_over_m_ddy;
    arma::cx_double i_dt_hb_over_2m_ddx;
    arma::cx_double i_dt_hb_over_2m_ddy;

public:
    arma::cx_mat psi;

    Solver(arma::mat,arma::mat,arma::mat,arma::mat,double,double,double);

// return the following state of the wave function
    void generateNextStep_FTCS ();
    void generateNextStep_BTCS ();
    void generateNextStep_CTCS ();
};

#endif // SOLVER_H
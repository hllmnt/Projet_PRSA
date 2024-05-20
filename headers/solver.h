#ifndef SOLVER_H
#define SOLVER_H
#include <armadillo>
#include "constants.h"

class Solver {
private:
// useful numerical values and matrices that only need to be computed once
    arma::cx_mat i_dt_over_hb_times_V_plus_i_dt_hb_over_m_ddx_plus_i_dt_hb_over_m_ddy;
    arma::cx_double i_dt_hb_over_2m_ddx;
    arma::cx_double i_dt_hb_over_2m_ddy;

// psi encercled by zeroes to make the submat operations in the solver more efficient
    arma::cx_mat extendedPsi;

public:
    arma::cx_mat psi;

    Solver(arma::cx_mat,arma::cx_mat,double,double,double,double);

// return the following state of the wave function
    void generateNextStep_FTCS ();
    void generateNextStep_BTCS ();
    void generateNextStep_CTCS ();
};

#endif // SOLVER_H
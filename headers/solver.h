#ifndef SOLVER_H
#define SOLVER_H
#include <armadillo>
#include "fdm.h"
#include "constantes.h"
#include "pre_computed.h"

class Solver {
private:
    const PreComputed* preComputed;
    const arma::cx_mat V;
    const unsigned int nbXPts;
    const unsigned int nbYPts;
    const double dx;
    const double dy;
    const double dt;
    const double m;

public:
    arma::cx_mat psi;

    Solver(PreComputed*,arma::cx_mat,arma::cx_mat,unsigned int,unsigned int,double,double,double,double);

    arma::cx_mat getPsi ();

    void generateNextStep_FTCS (); // return the following state of the wave function
    void generateNextStep_BTCS ();
    void generateNextStep_CTCS ();
};

#endif // SOLVER_H
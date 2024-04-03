#ifndef SOLVER_H
#define SOLVER_H
#include <armadillo>
#include "strategy.h"
#include "constantes.h"
#include "../headers/pre_computed.h"

class Solver {
private:
    const Strategy* strategy;
    const PreComputed* preComputed;
    const arma::mat V;
    const unsigned int nbXPts;
    const unsigned int nbYPts;
    const double dx;
    const double dy;
    const double dt;
    const double m;

public:
    arma::cx_mat psi;

    Solver(Strategy*,PreComputed*,arma::cx_mat,arma::mat,unsigned int,unsigned int,double,double,double,double);

    arma::cx_mat getPsi ();

    void generateNextStep (); // return the following state of the wave function
};

#endif // SOLVER_H

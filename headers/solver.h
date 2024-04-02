#ifndef SOLVER_H
#define SOLVER_H
#include <armadillo>

class Solver
{
public:
    Basis(double, double, int, double); // Constructor that initialize the parameters (ie mMax, nMax, n_zMax) to the correct values



    arma::mat generateNextStep (); // return the following state of 
};

#endif // SOLVER_H
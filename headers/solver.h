#ifndef SOLVER_H
#define SOLVER_H
#include <armadillo>
#include "strategy.h"

class Solver {
private:
    Strategy* strategy;

public:
    // TO DO more attributs

    Solver(Strategy* /* TO DO more arguments*/);

    arma::mat generateNextStep (); // return the following state of the wave function
};

#endif // SOLVER_H

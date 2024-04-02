#include "../headers/solver.h"

Solver::Solver(Strategy* strategy /*TO DO more arguments*/) : strategy(strategy) /*TO DO more arguments*/ {}

arma::mat Solver::generateNextStep() {
    return strategy->generateNextStep();
}
#include "../headers/solver.h"

Soulver::Solver(Strategy* strategy, PreComputed* preComputed arma::cx_mat psi, arma::mat V, 
                unsigned int nbXPts, unsigned int nbYPts, double dx, double dy, double dt, double mass)
            : strategy(strategy), preComputed(preComputed), psi(psi), V(V),
            nbXPts(nbXPts), nbYPts(nbYPts), dx(dx), dy(dy), dt(dt), mass(mass) {}

arma::cx_mat getPsi () {
    return psi;
}

void Solver::generateNextStep() {
    return strategy->generateNextStep();
}
#include <cxxtest/TestSuite.h>
#include <armadillo>
#include <cmath>
#include <iostream>
using namespace std;
#include "../headers/solver.h"
#include "../headers/constants.h"

class TestMethods : public CxxTest::TestSuite {
public:
    void test1 () {
        arma::cx_mat psi = {{arma::cx_double(0,0), arma::cx_double(0,0), arma::cx_double(0,0)},
                            {arma::cx_double(0,0), arma::cx_double(0,0), arma::cx_double(0,0)},
                            {arma::cx_double(0,0), arma::cx_double(0,0), arma::cx_double(0,0)}};
    
        arma::cx_mat V = {{arma::cx_double(0,0), arma::cx_double(0,0), arma::cx_double(0,0)},
                          {arma::cx_double(0,0), arma::cx_double(0,0), arma::cx_double(0,0)},
                          {arma::cx_double(0,0), arma::cx_double(0,0), arma::cx_double(0,0)}};

        double dx = 1.0;
        double dy = 1.0;
        double dt = 1.0;
        double m = 1.0;

        arma::cx_mat expectedPsi = {{arma::cx_double(0,0), arma::cx_double(0,0), arma::cx_double(0,0)},
                                    {arma::cx_double(0,0), arma::cx_double(0,0), arma::cx_double(0,0)},
                                    {arma::cx_double(0,0), arma::cx_double(0,0), arma::cx_double(0,0)}};

        Solver solver(psi, V, dx, dy, dt, m);

        solver.generateNextStep_FTCS();
        TS_ASSERT_DELTA(arma::norm(solver.psi - expectedPsi), 0.0, 1e-08);
    }

    void test2 () {
        arma::cx_mat psi = {{arma::cx_double(0,0),  arma::cx_double(0,0), arma::cx_double(0,0)},
                            {arma::cx_double(0,0),  arma::cx_double(1,0), arma::cx_double(0,0)},
                            {arma::cx_double(0,0),  arma::cx_double(0,0), arma::cx_double(0,0)}};

        arma::cx_mat V = {{arma::cx_double(0,0),  arma::cx_double(0,0), arma::cx_double(0,0)},
                          {arma::cx_double(0,0),  arma::cx_double(0,0), arma::cx_double(0,0)},
                          {arma::cx_double(0,0),  arma::cx_double(0,0), arma::cx_double(0,0)}};

        double dx = 1.0;
        double dy = 1.0;
        double dt = 1.0;
        double m = 1.0;

        arma::cx_mat expectedPsi = {{arma::cx_double(0,0),               arma::cx_double(0,Constants::hb/2), arma::cx_double(0,0)},
                                    {arma::cx_double(0,Constants::hb/2), arma::cx_double(1,-2),              arma::cx_double(0,Constants::hb/2)},
                                    {arma::cx_double(0,0),               arma::cx_double(0,Constants::hb/2), arma::cx_double(0,0)}};

        Solver solver(psi, V, dx, dy, dt, m);

        solver.generateNextStep_FTCS();
        TS_ASSERT_DELTA(arma::norm(solver.psi - expectedPsi), 0.0, 1e-08);
    }

    void test3 () {
        arma::cx_mat psi = {{arma::cx_double(0,0),  arma::cx_double(0,0), arma::cx_double(0,0)},
                            {arma::cx_double(0,0),  arma::cx_double(0,0), arma::cx_double(0,0)},
                            {arma::cx_double(0,0),  arma::cx_double(1,0), arma::cx_double(0,0)},
                            {arma::cx_double(0,0),  arma::cx_double(0,0), arma::cx_double(0,0)}};

        arma::cx_mat V = {{arma::cx_double(0,0),  arma::cx_double(0,0), arma::cx_double(0,0)},
                          {arma::cx_double(0,0),  arma::cx_double(0,0), arma::cx_double(0,0)},
                          {arma::cx_double(0,0),  arma::cx_double(0,0), arma::cx_double(0,0)},
                          {arma::cx_double(0,0),  arma::cx_double(0,0), arma::cx_double(0,0)}};

        double dx = 1.0;
        double dy = 1.0;
        double dt = 1.0;
        double m = 1.0;

        arma::cx_mat expectedPsi = {{arma::cx_double(0,0),               arma::cx_double(0,0),               arma::cx_double(0,0)},
                                    {arma::cx_double(0,0),               arma::cx_double(0,Constants::hb/2), arma::cx_double(0,0)},
                                    {arma::cx_double(0,Constants::hb/2), arma::cx_double(1,-2),              arma::cx_double(0,Constants::hb/2)},
                                    {arma::cx_double(0,0),               arma::cx_double(0,Constants::hb/2), arma::cx_double(0,0)}};

        Solver solver(psi, V, dx, dy, dt, m);

        solver.generateNextStep_FTCS();
        TS_ASSERT_DELTA(arma::norm(solver.psi - expectedPsi), 0.0, 1e-08);
    }
};

#include <cxxtest/TestSuite.h>
#include <armadillo>
#include <cmath>
#include <iostream>
using namespace std;
#include "../headers/solver.h"

#define FTCS
//#define BTCS
//#define CTCS

class TestMethods : public CxxTest::TestSuite {
public:
    #ifdef FTCS
    void testFtcs () {
        cout << "\nStarting FTCS test" << endl;
        arma::cx_mat V = {{arma::cx_double(0,0),  arma::cx_double(0,0), arma::cx_double(0,0)},
                          {arma::cx_double(0,0),  arma::cx_double(1,1), arma::cx_double(0,0)},
                          {arma::cx_double(0,0),  arma::cx_double(0,0), arma::cx_double(0,0)}};
        Solver solver();


        cout << "Finished FTCS test" << endl; 
    }
    #endif

    #ifdef BTCS
    void testBtcs () {
        // TO DO
    }
    #endif

    #ifdef CTCS
    void testCtcs () {
        // TO DO
    }
    #endif
};


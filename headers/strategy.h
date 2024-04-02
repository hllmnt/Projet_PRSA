#ifndef STRATEGY_H
#define STRATEGY_H
#include <armadillo>

class Strategy {
public:
    virtual arma::mat generateNextStep () = 0;
};

#endif // STRATEGY_H

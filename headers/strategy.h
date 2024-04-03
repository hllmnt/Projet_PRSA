#ifndef STRATEGY_H
#define STRATEGY_H
#include <armadillo>

class Strategy {
public:
    virtual void generateNextStep () = 0;
};

#endif // STRATEGY_H

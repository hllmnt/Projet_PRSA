#ifndef PRE_COMPUTED_H
#define PRE_COMPUTED_H
#include <iostream>
#include <armadillo>

class PreComputed {
public:
    const arma::cx_double i_dt_over_hb;
    const arma::cx_double i_dt_hb_over_m_ddx_plus_i_dt_hb_over_m_ddy;
    const arma::cx_double i_dt_hb_over_2m_ddx;
    const arma::cx_double i_dt_hb_over_2m_ddy;

    PreComputed (double,double,double,double);
};
#endif // PRE_COMPUTED_H
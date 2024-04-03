#include "../headers/constantes.h"
#include "../headers/pre_computed.h"

PreComputed::PreComputed(double dx, double dy, double dt, double m) :
    i_dt_over_hb(arma::cx_double(0, dt / Constantes::hb)),
    i_dt_hb_over_m_ddx_plus_i_dt_hb_over_m_ddy(arma::cx_double(0, dt * Constantes::hb) / (m * dx * dx) + arma::cx_double(0, dt * Constantes::hb) / (m * dy * dy))
    i_dt_hb_over_2m_ddx(arma::cx_double(0, dt * Constantes::hb) / (2 * m * dx * dx)),
    i_dt_hb_over_2m_ddy(arma::cx_double(0, dt * Constantes::hb) / (2 * m * dy * dy)) {}
#include "../headers/strategy.h"

class Ftcs : public Strategy {
public:
    void generateNextStep () override {


        psi += -(V * preComputed->i_dt_over_hb + preComputed->i_dt_hb_over_m_ddx_plus_i_dt_hb_over_m_ddy) * psi
                + preComputed->i_dt_hb_over_2m_ddx * ()
                + preComputed->i_dt_hb_over_2m_ddy * ()
    }
};
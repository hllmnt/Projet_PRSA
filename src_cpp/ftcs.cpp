#include "../headers/strategy.h"

class Ftcs : public Strategy {
public:
    void generateNextStep () override {
        arma::cx_mat psi_x_plus_dx = shift (psi,-1,0);
        psi_x_plus_dx.row(-1).zeros(); // the psi function is null when outside the matrix

        arma::cx_mat psi_x_minus_dx = shift (psi,1,0);
        psi_x_minus_dx.row(0).zeros();

        arma::cx_mat psi_y_plus_dy = shift (psi,-1,1);
        psi_y_plus_dy.col(-1).zeros();

        arma::cx_mat psi_y_minus_dy = shift (psi,1,1);
        psi_y_minus_dy.col(0).zeros();

        psi += -(preComputed->i_dt_over_hb * V + preComputed->i_dt_hb_over_m_ddx_plus_i_dt_hb_over_m_ddy) * psi
                + preComputed->i_dt_hb_over_2m_ddx * (psi_x_plus_dx + psi_x_minus_dx)
                + preComputed->i_dt_hb_over_2m_ddy * (psi_y_plus_dy + psi_y_minus_dy);
    }
};
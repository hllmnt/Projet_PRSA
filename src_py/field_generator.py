import initial_wave_function as iwf
import numpy as np
import potential as pt
import sys
import json
import matplotlib.pyplot as pl

input_json = json.load(open(sys.argv[1]))

nb_points_x = input_json["nb_points"]

xmax = input_json["xmax"]

x = np.linspace(-xmax, xmax, nb_points_x)
y = x

nb_steps = input_json["nb_steps"]
dt = input_json["dt"]
m = input_json["m"]

initial_wave_function = input_json["initial_wave_function"]
initial_wave_function_type = initial_wave_function["type"]

if initial_wave_function_type == "2D-HO":
    deg_array_x = initial_wave_function["deg_array_x"]
    deg_array_y = initial_wave_function["deg_array_y"]
    proportion_array = initial_wave_function["proportion_array"]
    w = initial_wave_function["w"]
    if type(deg_array_x) == int:
        deg_array_x = [deg_array_x]
        deg_array_y = [deg_array_y]
        proportion_array = [proportion_array]
    psi = iwf.solutionMix(np.array(deg_array_x), np.array(deg_array_y), np.array(proportion_array), x, y)

else:
    x0 = initial_wave_function["x0"]
    y0 = initial_wave_function["y0"]
    kx = initial_wave_function["kx"]
    ky = initial_wave_function["ky"]
    w = initial_wave_function["w"]
    psi = iwf.gaussian_packet(x, x0, y, y0, kx, ky, w)

method = input_json["method"]

potential = input_json["potential"]
potential_type = potential["type"]

if potential_type == "img":
    path = potential["path"]
    min = potential["min"]
    max = potential["max"]
    v = pt.from_img(path, min, max)

else:
    k = potential["k"]
    nx = potential["nx"]
    ny = potential["ny"]
    v = pt.from_formula(x, y, k, nx, ny)

fig = pl.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(x, y)
#plotting with colorbar
#adding lable and units
pl.xlabel('x [m]')
pl.ylabel('y [m]')
pl.clabel('psi [m^(-1/2)]')
pl.title('Wave function')
pl.colorbar(ax.plot_surface(X, Y, psi+v, cmap='viridis'))
pl.show()
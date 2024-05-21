import initial_wave_function as iwf
import numpy as np
import potential as pt
import sys
import json
import fun_db as fdb
import pymongo



default_path = "/".join(__file__.split("/")[:-2])

json_params = json.load(open(default_path + "/json/default.json"))

input_json = json.load(open(sys.argv[1]))

for key, value in input_json.items():
    json_params[key] = value

initial_wave_function = json_params.get("initial_wave_function")

iwf_type = initial_wave_function.get("type")

if iwf_type == "2D-HO":
    initial_wave_function = json.load(open(default_path + "/json/initial_wave_function/default_2D-HO.json"))

elif iwf_type == "gaussian":
    initial_wave_function = json.load(open(default_path + "/json/initial_wave_function/default_gaussian.json"))

else:
    raise ValueError("Invalid initial wave function type")

if input_json.get("initial_wave_function"):
    for key, value in input_json["initial_wave_function"].items():
        initial_wave_function[key] = value

potential = json_params.get("potential")

potential_type = potential.get("type")

if potential_type == "img":
    if potential.get("path") is None:
        raise ValueError("Path to image not provided")
    potential = json.load(open(default_path + "/json/potential/default_img.json"))

elif potential_type == "formula":
    potential = json.load(open(default_path + "/json/potential/default_formula.json"))


if input_json.get("potential"):
    for key, value in input_json["potential"].items():
        potential[key] = value

xmax = json_params["xmax"]
nb_points_x = json_params["nb_points_x"]

ymax = json_params["ymax"]
nb_points_y = json_params["nb_points_y"]

x = np.linspace(-xmax, xmax, nb_points_x)
y = np.linspace(-ymax, ymax, nb_points_y)

if iwf_type == "2D-HO":
    deg_x = initial_wave_function["deg_x"]
    deg_y = initial_wave_function["deg_y"]
    proportion_array = [k["n"]/k["d"] for k in initial_wave_function["proportion_array"]]
    w = initial_wave_function["w"]
    if type(deg_x) == int:
        deg_x = [deg_x]
        deg_y = [deg_y]
    psi = iwf.solutionMix(np.array(deg_x), np.array(deg_y), np.array(proportion_array), x, y, w)

elif iwf_type == "gaussian":
    x0 = initial_wave_function["x0"]
    y0 = initial_wave_function["y0"]
    kx = initial_wave_function["kx"]
    ky = initial_wave_function["ky"]
    w = initial_wave_function["w"]
    psi = iwf.gaussian_packet(x, x0, y, y0, kx, ky, w)
    psi = np.asfortranarray(psi)

if potential_type == "img":
    path = potential["path"]
    min = potential["min"]
    max = potential["max"]
    v = pt.from_img(path, min, max)

elif potential_type == "formula":
    k = potential["k"]["n"]/potential["k"]["d"]
    nx = potential["nx"]
    ny = potential["ny"]
    v = pt.from_formula(x, y, k, nx, ny)

else:
    v = np.zeros((nb_points_x, nb_points_y), dtype=np.complex128, order='F')


db = pymongo.MongoClient("mongodb://localhost:27017/")["PRSA"]

json_params["potential"] = v

exists, runID = fdb.checkExists(json_params, db)

if exists:
    print("Run already exists with ID: ", runID)

else:
    runID = fdb.createRun(json_params, db)

    print("Created run with ID: ", runID)

    dx = x[1] - x[0]
    dy = y[1] - y[0]

    norm = np.sum(psi*np.conj(psi))*dx*dy

    fdb.insert_mat(psi, norm.real, 0, runID, db)
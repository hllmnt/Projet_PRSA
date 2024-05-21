import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
target_dir = os.path.join(current_dir, "../bindings")
sys.path.append(target_dir)

import solver
import numpy as np
import pymongo
import fun_db as fdb
from tqdm import tqdm

def norm(psi, dx, dy):
    return np.sum(psi * np.conjugate(psi)).real * dx * dy

runID = int(sys.argv[1])

db = pymongo.MongoClient("mongodb://localhost:27017/")["PRSA"]

jsonParams, lastStepID = fdb.getRun(runID, db)

psi = fdb.get_one_mat(lastStepID, runID, db)

potential = jsonParams["potential"]
dx = 2*jsonParams["xmax"]/(jsonParams["nb_points_x"]-1)
dy = 2*jsonParams["ymax"]/(jsonParams["nb_points_y"]-1)
dt = jsonParams["dt"]
nb_steps = jsonParams["nb_steps"]
m = jsonParams["m"]
method = jsonParams["method"]

sol = solver.Solver(psi, potential, dx, dy, dt, m)

nb_remaining_steps = nb_steps - lastStepID

if method == "FTCS":
        for i in tqdm(range(nb_remaining_steps)):
                sol.generateNextStep_FTCS()
                lastStepID += 1
                fdb.insert_mat(sol.psi, norm(sol.psi, dx, dy), lastStepID, runID, db)
                fdb.updateLastStepID(runID, lastStepID, db)

elif method == "BTCS":
        for i in tqdm(range(nb_remaining_steps)):
                sol.generateNextStep_BTCS()
                lastStepID += 1
                fdb.insert_mat(sol.psi, norm(sol.psi, dx, dy), lastStepID, runID, db)
                fdb.updateLastStepID(runID, lastStepID, db)

elif method == "CTCS":
        for i in tqdm(range(nb_remaining_steps)):
                sol.generateNextStep_CTCS()
                lastStepID += 1
                fdb.insert_mat(sol.psi, norm(sol.psi, dx, dy), lastStepID, runID, db)
                fdb.updateLastStepID(runID, lastStepID, db)

else:
        raise ValueError("Invalid method")
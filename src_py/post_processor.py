#!/bin/python3
import pymongo
import numpy as np
import fun_db
import sys
from pyevtk.hl import imageToVTK


client=pymongo.MongoClient("mongodb://localhost:27017")
db=client["PRSA"]

if(len(sys.argv)!=2):
    print("Usage: {} RunID".format(sys.argv[0]))
    exit(1)

runID=sys.argv[1]

json= fun_db.getRun(runID,db)[0]

potential = json["potential"]
potential /= potential.max() + 1e-15

nx=json["nb_points_x"]
ny=json["nb_points_y"]

xmax=json["xmax"]
ymax=json["ymax"]

dx=2*xmax/nx
dy=2*ymax/ny


mlist=fun_db.get_mat(runID, db)

for i in mlist:
    filename="output_vtk/VAL{}_{}".format(runID,i["iteration"])

    N_=fun_db.fromBin(i["matrix"])
    N=np.abs(N_)
    imageToVTK(filename, origin = (-xmax, -ymax, 0.0),spacing = (dx, dy, 1.0) , pointData = {'N': N.astype(np.float32).reshape((nx,ny,1))})
    print("{}.vti generated".format(filename))



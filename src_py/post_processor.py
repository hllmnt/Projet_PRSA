#!/bin/python3
import pymongo
import numpy as np
import pickle
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

print(json)

nx=json["nb_points_x"]
ny=json["nb_points_y"]


mlist=fun_db.get_mat(runID, db)
print(mlist)
print(runID)

for i in mlist:
    filename="output_vtk/VAL{}_{}".format(runID,i["iteration"])


    N_=fun_db.fromBin(i["matrix"])
    N=np.abs(N_)
    imageToVTK(filename, pointData = {'N': N.astype(np.float32).reshape((nx,ny,1))})
    print("{}.vti generated".format(filename))



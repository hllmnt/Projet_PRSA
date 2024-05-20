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

col=db[runID]

json=db["JSON_COLLECTION"].find({"runID":runID})



mlist=col.find({})
print(mlist)
print(runID)

for i in mlist:
    print("test")
    filename="output_vtk/VAL{}_{}".format(runID,i["iteration"])

    N=fun_db.fromBin(i["matrix"])
    print(N)
    print(type(N));print("\n")
    N=N.reshape((2,1,2))
    print(N.shape)

    #imageToVTK(filename, pointData = {'N': N.astype(np.float32).reshape((nx, ny, 1), order = 'C')})
    imageToVTK(filename, pointData = {'N': N.reshape((2,2,1))})
    print("{}.vti generated".format(filename))



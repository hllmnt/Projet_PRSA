#!/bin/python3
import pymongo
import numpy as np
import pickle
import fun_db
import sys
from pyevtk.hl import imageToVTK


client=pymongo.MongoClient("mongodb://localhost:27017")
db=client["project_prsa"]
col=db["matrix"]

if(len(sys.argv)!=2):
    print("Usage: {} RunID".format(sys.argv[0]))
    exit(1)

identifier=sys.argv[1]

query={"id":int(identifier)}
mlist=col.find(query)
print(mlist)
print(identifier)

for i in mlist:
    print("test")
    if i["iteration"]==-1:
        filename="output_vtk/POT{}".format(identifier)
    else:
        filename="output_vtk/VAL{}_{}".format(identifier,i["iteration"])

    N=fun_db.fromBin(i["matrix"])
    print(N)
    print(type(N));print("\n")
    N=N.reshape((2,1,2))
    print(N.shape)
    nx=2
    ny=2
    

    #imageToVTK(filename, pointData = {'N': N.astype(np.float32).reshape((nx, ny, 1), order = 'C')})
    imageToVTK(filename, pointData = {'N': N.reshape((2,2,1))})
    print("{}.vti generated".format(filename))



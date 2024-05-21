#!/bin/python3
import pymongo
import numpy as np
import fun_db
import sys
import matplotlib.pyplot as pl

'''
Program to get a run from the database and plot the deviation of the norm from 1
'''

client=pymongo.MongoClient("mongodb://localhost:27017")
db=client["PRSA"]

if(len(sys.argv)!=2):
    print("Usage: {} RunID".format(sys.argv[0]))
    exit(1)

runID=sys.argv[1]

mlist=fun_db.get_mat(runID, db)

i=0
y = []

for value in mlist:
    norm = value["norm"]
    y.append(norm)
    i+=1

x = np.linspace(0,i-1,i)
y = np.abs(1 - np.array(y))

pl.plot(x,y)
pl.xlabel("Iteration")
pl.ylabel("Deviation from 1")
pl.show()

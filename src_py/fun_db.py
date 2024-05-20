import pymongo
import numpy as np
import pickle
import json
import hashlib

db = pymongo.MongoClient("mongodb://localhost:27017/")["PRSA"]

def toBin(x):
    '''Returns the data stored in x in a binary form'''
    return pickle.dumps(x)


def fromBin(x):
    '''Returns the data stored in binary form in x in its original form'''
    return pickle.loads(x)

def lastStep(runID,db):
    '''Get the value lastStepID from collection JSON_COLLECTION'''
    col = db["JSON_COLLECTION"]
    query = {"runID":runID}
    jlist = col.find(query)
    if len(jlist) == 0:
        return -1
    return jlist[0]["lastStepID"]

def lastRunID(db):
    '''Get the last runID from collection JSON_COLLECTION'''
    col = db["JSON_COLLECTION"]
    jlist = col.find().sort("runID", -1)
    if jlist.count() == 0:
        return 0
    return jlist[0]["runID"]

def createRun(jsonParams,db):
    '''Insert a new run in the collection JSON_COLLECTION'''
    col = db["JSON_COLLECTION"]
    runID = lastRunID() + 1
    x = toBin(jsonParams)
    col.insert_one({"runID":runID, "json":x, "lastStepID":0})
    return runID


def insert_mat(matrix_,norm,iteration,identifier,db):
    '''Inserts the matrix in the database'''
    col=db[identifier]
    matrix=toBin(matrix_)
    col.insert_one({"matrix":matrix, "iteration":iteration, "norm":norm})
    return


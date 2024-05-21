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
    maxID = col.find_one(sort=[("runID", -1)])
    if maxID == None:
        return 0
    return maxID["runID"]+1

def checkExists(jsonParams,db):
    '''Check if the run with the parameters jsonParams already exists in the collection JSON_COLLECTION'''
    col = db["JSON_COLLECTION"]
    x = toBin(jsonParams)
    query = {"json":x}
    res = col.find_one(query)
    if res == None:
        return False, -1
    return True, res["runID"]

def createRun(jsonParams,db):
    '''Insert a new run in the collection JSON_COLLECTION'''
    col = db["JSON_COLLECTION"]
    runID = lastRunID(db)
    x = toBin(jsonParams)
    col.insert_one({"runID":runID, "json":x, "lastStepID":0})
    return runID


def insert_mat(matrix_,norm,iteration,runID,db):
    '''Inserts the matrix in the database'''
    col=db["run_{}".format(runID)]
    matrix=toBin(matrix_)
    col.insert_one({"matrix":matrix, "iteration":iteration, "norm":norm})
    return

def get_one_mat(iteration,runID,db):
    '''gets one matrix from the corresponding run from the db'''
    col=db["run_{}".format(runID)]
    query={"iteration":iteration}
    matrix=col.find_one(query)
    return fromBin(matrix["matrix"])

def get_mat(runID,db):
    col=db["run_{}".format(runID)]
    mlist=col.find({})
    return mlist

def getRun(runID,db):
    '''Get the run with runID from the collection JSON_COLLECTION'''
    col = db["JSON_COLLECTION"]
    query = {"runID":runID}
    res = col.find_one(query)
    if res == None:
        raise Exception("Run with ID {} not found".format(runID))
    return fromBin(res["json"]), res["lastStepID"]


def updateLastStepID(runID, lastStepID, db):
    '''Update the lastStepID of the run with runID in the collection JSON_COLLECTION'''
    col = db["JSON_COLLECTION"]
    query = {"runID":runID}
    newvalues = {"$set": {"lastStepID":lastStepID}}
    col.update_one(query, newvalues)
    return

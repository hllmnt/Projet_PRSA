import pymongo
import numpy as np
import pickle
import json

client = pymongo.MongoClient("mongodb://localhost:27017/")

def toBin(x):
    return pickle.dumps(x)

def fromBin(x):
    return pickle.loads(x)

def lastStep(runID):
    '''Get the value lastStepID from collection JSON_COLLECTION'''
    db = client["PRSA"]
    col = db["JSON_COLLECTION"]
    query = {"runID":runID}
    jlist = col.find(query)
    if len(jlist) == 0:
        return -1
    return jlist[0]["lastStepID"]

def lastRunID():
    '''Get the last runID from collection JSON_COLLECTION'''
    db = client["PRSA"]
    col = db["JSON_COLLECTION"]
    jlist = col.find().sort("runID", -1)
    if jlist.count() == 0:
        return 0
    return jlist[0]["runID"]

def createRun(jsonParams):
    '''Insert a new run in the collection JSON_COLLECTION'''
    db = client["PRSA"]
    col = db["JSON_COLLECTION"]
    runID = lastRunID() + 1
    x = toBin(jsonParams)
    col.insert_one({"runID":runID, "json":x, "lastStepID":0})
    return True


def check_json(json_,database):

    x=toBin(json_)
    col=database["json"]
    query={"json":x}
    jlist=col.find(query)
    if(len(jlist)==1):
        return True
    return False

def insert_json(json_,identifier,database):

    return #TODO

def check_potential(identifier,database):

    return #TODO

def check_last_mat(identifier,database):

    return #TODO

def insert_mat(matrix,identifier,iteration,database):

    return #TODO

def insert_potential(matrix,identifier,database):

    return #TODO



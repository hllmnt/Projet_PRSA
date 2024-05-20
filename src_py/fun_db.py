import pymongo
import numpy as np
import pickle
import json
import hashlib

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

    json=toBin(json_)
    col=database["json"]
    query={"json":json}
    jlist=col.find(query)
    len=0
    for i in jlist:
        len+=1
    if(len==1):
        return True
    return False


def insert_json(json_,identifier,database):
    
    json=toBin(json_)
    col=database["json"]
    #identifier=hashlib.sha256(json).hexdigest()
    
    col.insert_one({"json":json, "id":identifier})
    return 


def check_last_mat(identifier,database):

    col=database["matrix"]
    query={"id":identifier}
    matlist=col.find(query)
    last_occurence=-2
    for i in matlist:
        if (i["itertion"]>last_occurence):
            last_occurence=i["itertion"]
    return last_occurence


def insert_mat(matrix_,identifier,iteration,database):

    col=database["matrix"]
    matrix=toBin(matrix_)
    col.insert_one({"matrix":matrix, "id":identifier, "itertion":iteration})

    return


def insert_potential(potential,identifier,database):

    insert_mat(potential,identifier,-1,database)

    return

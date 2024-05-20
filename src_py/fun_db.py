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

def check_last_mat(identifier,db):
    '''checks what was the last iteration in a run and returns its number'''
    col=db[identifier]
    matlist=col.find({})
    last_occurence=-2
    for i in matlist:
        if (i["iteration"]>last_occurence):
            last_occurence=i["iteration"]
        if (i["iteration"]>last_occurence):
            last_occurence=i["iteration"]
    return last_occurence


def insert_mat(matrix_,norm,iteration,identifier,db):
    '''Inserts the matrix in the database'''
    col=db[identifier]
    matrix=toBin(matrix_)
    col.insert_one({"matrix":matrix, "iteration":iteration, "norm":norm})
    return


def insert_potential(potential,norm,identifier,db):
    '''Inserts a potentials matrix into the database'''
    insert_mat(potential,norm,-1,identifier,db)

    return

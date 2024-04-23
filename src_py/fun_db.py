import pymongo
import numpy as np
import pickle
import json

def toBin(x):
    return pickle.dumps(x)

def fromBin(x):
    return pickle.loads(x)

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



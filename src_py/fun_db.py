import pymongo
import numpy as np
import pickle
import json

def toBin(x):
    return pickle.dumps(x)


def fromBin(x):
    return pickle.loads(x)


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
    col.insert_one({"json":json, "id":identifier})
    return 


def check_last_mat(identifier,collection,database):

    col=database[collection]
    query={"id":identifier}
    matlist=col.find(query)
    last_occurence=-2
    for i in matlist:
        if (i["iteration"]>last_occurence):
            last_occurence=i["iteration"]
    return last_occurence


def insert_mat(matrix_,identifier,iteration,collection,database):

    col=database[collection]
    matrix=toBin(matrix_)
    col.insert_one({"matrix":matrix, "id":identifier, "iteration":iteration})

    return


def insert_potential(potential,identifier,database):

    insert_mat(potential,identifier,-1,database)

    return

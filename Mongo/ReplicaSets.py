'''
Created on Feb 18, 2016

@author: usreei
'''
from pymongo import MongoClient

#===============================================================================
# #Starting the replica set mongod instances
# $ mkdir -p /data/db0 /data/db1 /data/db2
# $ mongod --port 27017 --dbpath /data/db0 --replSet foo
# $ mongod --port 27018 --dbpath /data/db1 --replSet foo
# $ mongod --port 27019 --dbpath /data/db2 --replSet foo
#===============================================================================

#Initializing the set
c = MongoClient('localhost', 27017)

config = {'_id': 'foo', 'members': [
    {'_id': 0, 'host': 'localhost:27017'},
    {'_id': 1, 'host': 'localhost:27018'},
    {'_id': 2, 'host': 'localhost:27019'}]}

c.admin.command("replSetInitiate", config)
#===============================================================================
# OUTPUT - {'info': 'Config now saved locally.  Should come online in about a
# minute.', 'ok': 1.0}
#===============================================================================

#Connecting to the Replica set
MongoClient('localhost', replicaset='foo')

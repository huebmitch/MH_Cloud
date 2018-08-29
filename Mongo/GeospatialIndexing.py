'''
Created on Feb 18, 2016

@author: usreei
'''

#===============================================================================
# This is an example
#===============================================================================

#Creating a Geospatial Index

from pymongo import MongoClient, GEO2D
from bson.son import SON

db = MongoClient().geo_example
db.places.create_index([("loc", GEO2D)])
u'loc_2d'

#Inserting Places
result = db.places.insert_many([{"loc": [2, 5]},
                                {"loc": [30, 5]},
                                {"loc": [1, 2]},
                                {"loc": [4, 4]}])

#Querying -$near
for doc in db.places.find({"loc": {"$near": [3, 6]}}).limit(3):
    repr(doc)

#Querying -$maxDistance
query = {"loc": SON([("$near", [3, 6]), ("$maxDistance", 100)])}
for doc in db.places.find(query).limit(3):
    repr(doc)

#Querying -$box -Given Rectangle (specified by lower-left and upper-right coordinates)
query = {"loc": {"$within": {"$box": [[2, 2], [5, 6]]}}}
for doc in db.places.find(query).sort('_id'):
    repr(doc)

#Querying -$center -Circle (specified by center point and radius)
query = {"loc": {"$within": {"$center": [[0, 0], 6]}}}
for doc in db.places.find(query).sort('_id'):
    repr(doc)

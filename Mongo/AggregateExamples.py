'''
Created on Feb 17, 2016

@author: usreei
'''

#Imports
from bson.son import SON

#SETUP - Inserting Bulk data for aggregation example
from pymongo import MongoClient
db = MongoClient().aggregation_example
result = db.things.insert_many([{"x": 1, "tags": ["dog", "cat"]},
                                {"x": 2, "tags": ["cat"]},
                                {"x": 2, "tags": ["mouse", "cat", "dog"]},
                                {"x": 3, "tags": []}])
result.inserted_ids

#===============================================================================
# OUTPUT
# [ObjectId('56c4cfdcbaa0af0c3c9f4729'),ObjectId('56c4cfdcbaa0af0c3c9f472a'),
#  ObjectId('56c4cfdcbaa0af0c3c9f472b'), ObjectId('56c4cfdcbaa0af0c3c9f472c')]
#===============================================================================

#Aggregate Framework
pipeline = [
    {"$unwind": "$tags"},
    {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])}
]
list(db.things.aggregate(pipeline))
#===============================================================================
# OUTPUT [{'_id': 'cat', 'count': 3}, {'_id': 'dog', 'count': 2}, {'_id':
# 'mouse', 'count': 1}]
#===============================================================================

#To run an explain on the aggregate and pipeline
db.command('aggregate', 'things', pipeline=pipeline, explain=True)

'''
Created on Feb 17, 2016

@author: usreei
'''

#Starting in the Python Console
from pymongo import MongoClient

#Make connection to MongoD
client = MongoClient('localhost', 27017)

#Selecting the Database for authentication
db = client.authdb  # authdb will change depending on which db you authenticate against

#Authenticating
db.authenticate('user', 'password', source='source_database')

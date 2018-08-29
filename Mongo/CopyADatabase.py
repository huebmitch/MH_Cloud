'''
Created on Feb 18, 2016

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

client.admin.command('copydb',
                     fromdb='source_db_name',
                     todb='target_db_name')

#===============================================================================
# OUTPUT = {'ok' : 1} if SUCCESSFUL
#===============================================================================

#Copying a database from a server that is password-protected.
#If the source server is password-protected, use the copyDatabase function in the mongo shell.
#https://docs.mongodb.org/manual/reference/method/db.copyDatabase/

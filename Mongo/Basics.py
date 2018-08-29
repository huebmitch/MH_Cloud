##Importing Resources
import datetime

from pymongo import MongoClient


##    From bson.objectid import ObjectId

##    Make connection to MongoD
client = MongoClient('localhost', 27017)

##Selecting the Database for authentication
db = client.authdb

##Authenticating
db.authenticate('user', 'password', source='source_database')

##Selecting the Database to work with
db = client.test

##List all Collections in DB
db.collection_names(include_system_collections=False)

##Selecting the Collection
collection = db.posts

##Document
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

##Inserting a Document
posts = db.posts
post_id = posts.insert_one(post)
# # post_id = posts.insert_one(post).insert_id #errored Out
#
#
#      #Checking the insert_one(post)
# post_id #error out

#Getting a document with find_one()
posts.find_one()

##find_one() with arguments for example
posts.find_one({"author": "Mike"})
posts.find_one({"_id": post_id})

#     # The web framework gets post_id from the
#     # URL and passes it as a string
# def get(post_id):
#     # Convert from string to ObjectId:
#     document = client.db.collection.find_one({'_id': ObjectId(post_id)})

# Bulk Insertion
new_posts = [{"author": "Mike",
              "text": "Another post!",
              "tags": ["bulk", "insert"],
              "date": datetime.datetime(2009, 11, 12, 11, 14)},

             {"author": "Eliot",
              "title": "MongoDB is fun",
              "text": "and pretty easy too!",
              "date": datetime.datetime(2009, 11, 10, 10, 45)}]

result = posts.insert_many(new_posts)
result.inserted_ids

##Querying for more than one document
for post in posts.find():
    print(post)

for post in posts.find({"author": "Mike"}):
    print(post)

##Counting Documents
posts.count()

posts.find({"author": "Mike"}).count()

##Range Queries
d = datetime.datetime(2009, 11, 12, 12)
for post in posts.find({"date": {"$lt": d}}).sort("author"):
    print(post)

    ##Indexing
result = db.profiles.create_index('user_id', unique=True)

list(db.profiles.index_information())

##Index prevents inserting duplicate user_id in collection
user_profiles = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Ziltoid'}]
result = db.profiles.insert_many(user_profiles)

new_profile = {'user_id': 213, 'name': 'Drew'}
duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
result = db.profiles.insert_one(new_profile)  # This is fine.
result = db.profiles.insert_one(duplicate_profile)  # This will error out

##Adding DateTime to posts
##This will add a document to the collection with the time in UTC
result = db.posts.insert_one(
    {"last_modified": datetime.datetime.utcnow()})

from pymongo import MongoClient

uri = "mongodb://localhost:27017/test"
client = MongoClient(uri)
database = client.get_database()

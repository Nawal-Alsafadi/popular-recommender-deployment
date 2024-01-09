from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.myDB
vol = db.myCollection 


def make_db_connection():
    client = MongoClient('localhost', 27017)
    return access_db(client=client)


def access_db(client: MongoClient):
    db = client["myDB"]
    return db

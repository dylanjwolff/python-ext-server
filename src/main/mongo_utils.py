""" mongo client """
import os
import logging
from pymongo import MongoClient

def discover_mongo_uri():
    """ get mongo uri """
    host = os.environ['MONGO_SERVICE_HOST']
    port = os.environ['MONGO_SERVICE_PORT']
    return "mongodb://" + host + ":" + port

def build_mongo_collection():
    """ get mongo collection """
    try:
        client = MongoClient(discover_mongo_uri())
    except:
        logging.warn("Exception discovering db");
        return build_mock_mongo_collection()
    datab = client.test_database
    return datab.test_collection

def build_mock_mongo_collection():
    """ get mock mongo collection """
    mock_collection = lambda: None
    mock_collection.insert_one = lambda x: None
    return mock_collection

def build_mock_mongo():
    """ get mock mongo """
    mongo = lambda: None
    mongo.db = lambda: None
    mongo.db.data = build_mock_mongo_collection()
    return mongo

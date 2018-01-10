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
        mock_collection = lambda: None
        mock_collection.insert_one = lambda x: None
        return mock_collection
    datab = client.test_database
    return datab.test_collection

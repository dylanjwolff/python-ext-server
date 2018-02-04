""" Server module """
import logging
import json
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS, cross_origin

import mongo_utils

APP = Flask(__name__)
CORS_APP = CORS(APP)
APP.config['CORS_HEADERS'] = "Content-Type"

try:
    APP.config['MONGO_URI'] = mongo_utils.discover_mongo_uri()
    MONGO = PyMongo(APP)
except:
    logging.warn("Exception discovering db")
    MONGO = mongo_utils.build_mock_mongo()

@APP.route('/', methods=['POST'])
def add_base():
    """ adds base POST method """
    jsonreq = request.get_json()
    in_resp = MONGO.db.data.insert_one(jsonreq)
    jsonreq["_id"] = str(jsonreq["_id"])
    return jsonify(jsonreq)

if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0', port=8080)

""" Server module """
import logging
from flask import Flask
from flask import jsonify
from flask import request

import mongo_utils

APP = Flask(__name__)
DB_COL = mongo_utils.build_mongo_collection()

@APP.route('/', methods=['POST'])
def add_base():
    """ adds base POST method """
    DB_COL.insert_one(request.get_json())
    logging.info('adding POST')
    return jsonify(request.get_json())


if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0', port=80)

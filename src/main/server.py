""" Server module """
import logging
from flask import Flask
from flask import jsonify
from flask import request

APP = Flask(__name__)

APP.config['MONGO_DBNAME'] = 'restdb'
APP.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

@APP.route('/', methods=['POST'])
def add_base():
    """ adds base POST method """
    logging.info('adding POST')
    return jsonify({'result' : 'yay'})

if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0', port=80)

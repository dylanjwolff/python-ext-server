""" Tests for server """
import unittest
import logging
import sys
from flask import request
from flask import jsonify

import server

class TestApiMethods(unittest.TestCase):
    """ Test class for Server """

    def test_post(self):
        """ test the POST method """
        with server.APP.test_request_context('/', method='POST', data={"test": "req"}):
            response = server.APP.dispatch_request()
            self.assertEqual("fail", response.get_data())

if __name__ == '__main__':
    unittest.main()

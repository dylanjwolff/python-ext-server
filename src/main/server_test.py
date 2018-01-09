""" Tests for server """
import unittest
import logging
import sys
from flask import request
from flask import jsonify

import server
class TestApiMethods(unittest.TestCase):
    """ Test class for Server """

    def setUp(self):
        print('wtf')
        logging.info("Setting up for tests")

    def test_post(self):
        """ test the POST method """
        with server.APP.test_request_context('/', method='POST'):
            response = server.APP.dispatch_request()
            self.assertEqual("fail", response.get_data())

    def test_post_alt(self):
        """ test the POST method alt"""
        with server.APP.test_client() as app:
            response = app.post('/', data="test")
            self.assertEqual("fail", response)


if __name__ == '__main__':
    unittest.main()

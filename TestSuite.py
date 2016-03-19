__author__ = 'zhangb3'

import unittest
import os
import requests
from fibonacciArray import FibonacciArray

request_cmd = "http"
url = "http://127.0.0.1:8000/fibonacci/"

class FunctionTest(unittest.TestCase):

    def test_get_first_element(self):
        """Get first element of fibonacci Array"""
        myurl = url + "1"
        myrequest = requests.get(myurl)
        print "response content is %s, return code is %s" % (myrequest.content, myrequest.status_code)
        self.assertEqual(myrequest.status_code, 200)

    def test_get_two_elements(self):
        """Get first 2 elements of fibonacci Array"""
        myurl = url + "2"
        myrequest = requests.get(myurl)
        print "response content is %s, return code is %s" % (myrequest.content, myrequest.status_code)
        self.assertEqual(myrequest.status_code, 200)

    def test_regular_number(self):
        """Get first 2 elements of fibonacci Array"""
        myurl = url + "25"
        myrequest = requests.get(myurl)
        print "response content is %s, return code is %s" % (myrequest.content, myrequest.status_code)
        self.assertEqual(myrequest.status_code, 200)

    def test_maximum_number(self):
        """Get maximum elements of fibonacci Array"""
        myurl = url + "5000"
        myrequest = requests.get(myurl)
        print "response content is %s, return code is %s" % (myrequest.content, myrequest.status_code)
        self.assertEqual(myrequest.status_code, 200)

class NegativeTest(unittest.TestCase):
    def test_zeor(self):
        myurl = url + "0"
        myrequest = requests.get(myurl)
        print "response content is %s, return code is %s" % (myrequest.content, myrequest.status_code)
        self.assertTrue("negative integer is not allowed" in myrequest.content)

    def test_negative_integer(self):
        myurl = url + "-5"
        myrequest = requests.get(myurl)
        print "response content is %s, return code is %s" % (myrequest.content, myrequest.status_code)
        self.assertTrue("negative integer is not allowed" in myrequest.content)

    def test_other_types(self):
        myurl = url + "string"
        myrequest = requests.get(myurl)
        print "response content is %s, return code is %s" % (myrequest.content, myrequest.status_code)
        self.assertTrue("The number you input is not right, an integer is expected" in myrequest.content)

    def test_exceed_maximum(self):
        myurl = url + "5001"
        myrequest = requests.get(myurl)
        print "response content is %s, return code is %s" % (myrequest.content, myrequest.status_code)
        self.assertTrue("The number is bigger than maximum limitation 5000" in myrequest.content)

if __name__ == '__main__':
    unittest.main()

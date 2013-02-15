"""
Additional functional tests following a format similar to that of testSimple.py
"""

import unittest
import os
import testLib

class TestLogin(testLib.RestTestCase):
    """Issue a REST API request to run the unit tests, and analyze the result"""
    def assertResponse(self, respData, count, errCode):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)
    
    def testLogin1(self):
        respData = self.makeRequest("/users/login", method="POST",
                                    data = {'user':'harry', 'password':'potter'})
        self.assertResponse(respData, None, testLib.RestTestCase.ERR_BAD_CREDENTIALS)

    def testLogin2(self):
        self.makeRequest("/users/add", method="POST",
                                    data = {'user':'ron', 'password':'weasley'})
        respData = self.makeRequest("/users/login", method="POST",
                                    data = {'user':'ron', 'password':'ginny'})
        self.assertResponse(respData, None, testLib.RestTestCase.ERR_BAD_CREDENTIALS)

    def testLogin3(self):
        self.makeRequest("/users/add", method="POST",
                                    data = {'user':'fred', 'password':'weasley'})
        respData = self.makeRequest("/users/login", method="POST",
                                    data = {'user':'george', 'password':'weasley'})
        self.assertResponse(respData, None, testLib.RestTestCase.ERR_BAD_CREDENTIALS)
 
    def testLogin4(self):
        self.makeRequest("/users/add", method="POST",
                                    data = {'user':'hermione', 'password':'granger'})
        respData = self.makeRequest("/users/login", method="POST",
                                    data = {'user':'hermione', 'password':'granger'})
        respData = self.makeRequest("/users/login", method="POST",
                                    data = {'user':'hermione', 'password':'granger'})
        respData = self.makeRequest("/users/login", method="POST",
                                    data = {'user':'hermione', 'password':'granger'})
        self.assertResponse(respData, 4, testLib.RestTestCase.SUCCESS)

    def testLogin5(self):
        self.makeRequest("/users/add", method="POST",
                         data = {'user':'tom', 'password':'riddle'})
        respData = self.makeRequest("/users/login", method="POST",
                                    data = {'user':'lord', 'password':'voldemort'}) 
        self.assertResponse(respData, None, testLib.RestTestCase.ERR_BAD_CREDENTIALS)

    
class TestAdd(testLib.RestTestCase):
    """Test adding users"""
    def assertResponse(self, respData, count, errCode):
        """
        Check that the response data dictionary matches the expected values
        """
        expected = { 'errCode' : errCode }
        if count is not None:
            expected['count']  = count
        self.assertDictEqual(expected, respData)

    def testAddUser1(self):
        respData = self.makeRequest("/users/add", method="POST",
                                    data = {'user':'arcade', 'password':'fire'})
        respData = self.makeRequest("/users/add", method="POST",
                                    data = {'user':'arcade', 'password':'games'})
        self.assertResponse(respData, None, testLib.RestTestCase.ERR_USER_EXISTS)

    def testAddUser2(self):
        respData = self.makeRequest("/users/add", method="POST",
                                    data = {'user':'', 'password':'MGMT'})
        self.assertResponse(respData, None, testLib.RestTestCase.ERR_BAD_USERNAME)

    def testAddUser3(self):
        respData = self.makeRequest("/users/add", method="POST",
                                    data = {'user':'ok'*128, 'password':'go'})
        self.assertResponse(respData, None, testLib.RestTestCase.ERR_BAD_USERNAME)

    def testAddUser4(self):
        respData = self.makeRequest("/users/add", method="POST",
                                    data = {'user':'MVOTC', 'password':''})
        self.assertResponse(respData, 1, testLib.RestTestCase.SUCCESS)

    def testAddUser5(self):
        respData = self.makeRequest("/users/add", method="POST",
                                    data = {'user':'tswift', 'password':'trouble'*128})
        self.assertResponse(respData, None, testLib.RestTestCase.ERR_BAD_PASSWORD)

    

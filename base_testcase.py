'''
Created on Jun 8, 2016

@author: rkushchak
'''
import unittest
import ConfigParser
from selenium import webdriver
#import testing

class BaseTestCase(unittest.TestCase):
    def Setup (self):
        __SECTION = 'testing'
        config = ConfigParser.ConfigParser()
        config.readfp(open('testing.ini'))
        self.browser = config.get(__SECTION, 'browser')
        if self.__browser == "chrome":
            self.driver = webdriver.Chrome ()
        elif self.__browser == "firefox":
            self. driver = webdriver.Firefox ()

class LoginTest(BaseTestCase):
    
    def setUp(self):
        BaseTestCase.setUp(self)
        self.driver.get(_url)

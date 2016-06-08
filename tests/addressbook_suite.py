'''
Created on Jun 6, 2016

@author: rkushchak
'''

import unittest
import test_login_page
import test_navigation
import test_delete_new_record
from selenium import webdriver
import sys

browsers = {"firefox": webdriver.Firefox, "chrome": webdriver.Chrome, "safari": webdriver.Safari}

def suite():
    return unittest.TestSuite((\
        unittest.makeSuite(test_login_page.LoginTest),
        unittest.makeSuite(test_navigation.NavigationTest),
        unittest.makeSuite(test_delete_new_record.Add_Remove_Test),
        ))

import time
import HTMLTestRunner
def run(suite, report = "/home/rkushchak/workspace/addressbook/tests/reports/test_reports_%s.html" % time.asctime()):
        with open(report, "w") as f:
            HTMLTestRunner.HTMLTestRunner(
                    stream = f,
                    title = 'Selenium Test',
                    verbosity = 2,
                    description = 'Selenium Test'
                    ).run(suite)

if __name__ == "__main__":
    
    browsername = "chrome"
    if len(sys.argv) == 2:
        browsername = sys.argv[1].lower()
    browser = browsers[browsername]
    unittest.main(run(suite()))
    
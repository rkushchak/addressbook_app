'''
Created on May 10, 2016

@author: rkushchak
'''
import unittest
import tests.HTMLTestRunner
from selenium import webdriver
import sys
import tests.test_login_page
import tests.test_navigation
import tests.test_delete_new_record

browsers = {"firefox": webdriver.Firefox, "ie": webdriver.Ie, "chrome": webdriver.Chrome, "safari": webdriver.Safari}

#suite = unittest.TestLoader().loadTestsFromTestCase(test_addressbook.AddressbookTests)
#unittest.TextTestRunner(verbosity=2).run(suite)
def suite():
    s1 = unittest.TestLoader().loadTestsFromTestCase(tests.test_login_page)
    s2 = unittest.TestLoader().loadTestsFromTestCase(tests.test_navigation)
    s3 = unittest.TestLoader().loadTestsFromTestCase(tests.test_delete_new_record)
    return unittest.TestSuite([s1,s2,s3])

#This function declares the Test Results and stores them in /home/rkushchak/workspace/addressbook/tests/
def run(suite, report = "/home/rkushchak/workspace/addressbook/tests/test_reports.html"):
    with open(report, "w") as f:
        tests.HTMLTestRunner.HTMLTestRunner(
                    stream = f,
                    title = 'Selenium Test',
                    verbosity = 2,
                    description = 'Selenium Test'
                    ).run(suite)

if __name__ == "__main__":
    browsername = "firefox"
    if len(sys.argv) == 2:
        browsername = sys.argv[1].lower()
    browser = browsers[browsername]
    run(suite())        



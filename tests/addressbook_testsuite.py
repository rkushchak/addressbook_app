'''
Created on May 10, 2016

@author: rkushchak
'''
import unittest
import HTMLTestRunner
from selenium import webdriver
import sys
from test_addressbook import AddressbookTests 

browsers = {"firefox": webdriver.Firefox, "ie": webdriver.Ie, "chrome": webdriver.Chrome, "safari": webdriver.Safari}

#suite = unittest.TestLoader().loadTestsFromTestCase(test_addressbook.AddressbookTests)
#unittest.TextTestRunner(verbosity=2).run(suite)
def suite():
    s1 = unittest.TestLoader().loadTestsFromTestCase(AddressbookTests)
    return unittest.TestSuite([s1])

#This function declares the Test Results and stores them in /home/rkushchak/workspace/addressbook/tests/
def run(suite, report = "/home/rkushchak/workspace/addressbook/tests/test_reports.html"):
    with open(report, "w") as f:
        HTMLTestRunner.HTMLTestRunner(
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
"""
if __name__ == "__main__":
    unittest.main()
"""
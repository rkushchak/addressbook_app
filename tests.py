'''
Created on May 10, 2016

@author: rkushchak
'''
import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pages


class AddressbookLoginTestCase(unittest.TestCase):
    
    def setUp(self): 
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 100)
        self.driver.get("http://localhost/index.php")
         
    def test_login_smoketest(self):
        login_page = pages.LoginPage(self.driver)
        self.assertTrue(login_page.is_title(), "addressbook application title doesn't match.")
        login_page.login('admin', 'secret')
        #self.assertTrue(login_page.get_login('admin')and login_page.get_password('secret'))
        self.assertTrue('admin', login_page.get_login) and self.assertTrue('secret', login_page.get_password)
              
        login_page.click_submit()
        

    def test_navi(self): 
        self.test_login_smoketest()   
        page_navi = pages.PageNavi(self.driver)
        page_navi.navigation()
        
        
    def tearDown(self):
        self.driver.close()
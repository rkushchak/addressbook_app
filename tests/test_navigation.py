'''
Created on Jun 6, 2016

@author: rkushchak
'''

import unittest
from selenium import webdriver
import properties
from page import LoginPage,PageNavi

#user = properties.user
#password = properties.password
#_url = properties._url

class NavigationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(properties._url)
        self.login_page = LoginPage(self.driver)
        self.login_page.login(properties.user, properties.password)
        self.login_page.click_submit()
        
    #def test_login(self):
        #self.login_page
        #login_page = LoginPage(self.driver)
        #login_page.login(user, password)
        #login_page.click_submit()
        
    def test_navigation(self):
        self.login_page 
        page_navi = PageNavi(self.driver)
        page_navi.navigation()
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
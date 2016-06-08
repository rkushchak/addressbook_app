'''
Created on Jun 6, 2016

@author: rkushchak
'''

from page import LoginPage
import unittest
from selenium import webdriver
import properties


user = properties.user #user = 'admin'
password = properties.password #password = 'secret' 
_url = properties._url #_url = "http://localhost/index.php"

class LoginTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver.set_window_size(1380, 880)
        self.driver.get(_url)   
        

    def test_login_page(self):
        login_page = LoginPage(self.driver)
        login_page.login(user, password)
        login_page.click_submit()
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

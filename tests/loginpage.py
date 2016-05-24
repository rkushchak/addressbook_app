'''
Created on Apr 26, 2016

@author: rkushchak
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class LoginAddressbook(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 100)

    def test_login_in_addressbook(self):
        driver = self.driver
        driver.get("http://localhost:80/index.php")
        self.assertIn("Address book", driver.title) # assertion word "Addressbook" is in title 
        # find username field and send key value
        username = driver.find_element_by_name("user")
        username.send_keys("admin")
        
        # find password field and send key value 
        password = driver.find_element_by_name("pass")
        password.send_keys("secret")
        # Login to Addressbook
        submit_button = driver.find_element_by_xpath('.//*[@id="LoginForm"]/input[3]')
        submit_button.click() # password.submit()
        
        # Navigate to Home
        home_link = driver.find_element_by_link_text('home')
        home_link.click()
        # Navigate to Add New       
        add_link = driver.find_element_by_link_text('add new')
        add_link.click()
        # Navigate to Groups
        groups_link = driver.find_element_by_link_text('groups')
        groups_link.click()
        # Navigate to Birthdays
        birthdays_link = driver.find_element_by_link_text('next birthdays')
        birthdays_link.click()
        ## Navigate to Maps
        maplink = driver.find_element_by_link_text('map')
        maplink.click()
        # Navigate to Import
        import_link = driver.find_element_by_link_text('import')
        import_link.click()
        # Navigate to Export
        export_link = driver.find_element_by_link_text('export')
        export_link.click()
        # Navigate to Print All
        print_link = driver.find_element_by_link_text('print all')
        print_link.send_keys(Keys.BACKSPACE)
        
        # Navigate to Print Phones
        printph_link = driver.find_element_by_link_text('print phones')
        printph_link.send_keys(Keys.BACKSPACE)
        # Logout from AddressBook
        logout_link = driver.find_element_by_link_text('Logout')
        logout_link.click()
        

    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()
'''
Created on Jun 6, 2016

@author: rkushchak
'''
from page import LoginPage,MainPage,PageNavi,AddNew
import random_test_data
import properties

import unittest
from selenium import webdriver

class Add_Remove_Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(properties._url)
        
        self.login_page = LoginPage(self.driver)
        self.login_page.login(properties.user, properties.password)
        self.login_page.click_submit()
            
        
    #def test_login(self):
        #self.login_page
        
    
    def test_delete_new_record(self): 
        self.login_page 
        add_new_lnk = PageNavi(self.driver)
        add_new_lnk.add_lnk() #click on add new link 
       
        page_add_new = AddNew(self.driver)
        # filling Address on second page on Add new page
        page_add_new.fill_address(random_test_data.random_letters(5)) and self.assertTrue(random_test_data.random_letters(5)) # fill the address field
        page_add_new.click_next # navigate to next page
        
        # Filling user data
        page_add_new.fill_user_name(properties.f_name, properties.m_name, properties.l_name) 
        self.assertTrue(properties.f_name) and self.assertTrue(properties.m_name) and self.assertTrue(properties.l_name) 
        page_add_new.set_email(properties.e_mail) and self.assertTrue(properties.e_mail) 
        page_add_new.set_phone('+' + properties.phone_number) and self.assertTrue('+' + properties.phone_number)
        
        page_add_new.click_enter() 
        self.driver.implicitly_wait(10)
               
        # Search on the main page        
        main_page = MainPage(self.driver)
        main_page.search_element(properties.phone_number) and self.assertTrue(properties.phone_number)
        #self.driver.implicitly_wait(10)
        main_page.select_all_element()
        main_page.delete_bttn()
        
        main_page.accept_alert()
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
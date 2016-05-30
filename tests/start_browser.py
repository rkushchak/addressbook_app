import sys
import unittest

from selenium import webdriver
import HTMLTestRunner
import page
import random_test_data

browsers = {"firefox": webdriver.Firefox, "ie": webdriver.Ie, "chrome": webdriver.Chrome, "safari": webdriver.Safari}

class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.set_window_size(1380, 880)
        self.driver.get("http://localhost/index.php")   
        ''' login to addressbook ''' 
        self.user = 'admin' # user name login
        self.password = 'secret' # user password login 
        self.login_page = page.LoginPage(self.driver)
        self.login_page.login(self.user, self.password)
        self.login_page.click_submit()
        #random data
        ''' random data'''
        self.e_mail = (random_test_data.random_letters(6) + '@' + random_test_data.random_letters(5) + '.com') # generate random email
        self.phone_number = random_test_data.random_number(11)  # generate random phone number
        self.f_name = random_test_data.random_letters(6) # generate First name
        self.m_name = random_test_data.random_letters(5) # generate Middle name
        self.l_name = random_test_data.random_letters(7) # generate Last name

    def test_login_page(self):
        self.login_page 
    
    def test_navi(self): 
        self.login_page 
        #self.test_login_page()   
        page_navi = page.PageNavi(self.driver)
        page_navi.navigation()
    
    def test_add_new_record_and_delete_it(self): 
        #self.login_page
        self.test_login_page() # login to addressbook
        add_new_lnk = page.PageNavi(self.driver)
        add_new_lnk.add_lnk() #click on add new link 
        
        page_add_new = page.AddNew(self.driver)
        # filling Address on second page on Add new page
        page_add_new.fill_address(random_test_data.random_letters(5)) and self.assertTrue(random_test_data.random_letters(5)) # fill the address field
        page_add_new.click_next # navigate to next page
        
        # Filling user data
        page_add_new.fill_user_name(self.f_name,self.m_name,self.l_name) 
        self.assertTrue(self.f_name) and self.assertTrue(self.m_name) and self.assertTrue(self.l_name) 
        page_add_new.set_email(self.e_mail) and self.assertTrue(self.e_mail) 
        page_add_new.set_phone('+' + self.phone_number) and self.assertTrue('+' + self.phone_number)
        
        page_add_new.click_enter() 
        self.driver.implicitly_wait(10)
               
        # Search on the main page        
        main_page = page.MainPage(self.driver)
        main_page.search_element(self.phone_number) and self.assertTrue(self.phone_number)
        #self.driver.implicitly_wait(10)
        main_page.select_all_element()
        main_page.delete_bttn()
        
        main_page.accept_alert()
    
    
    def tearDown(self):
        self.driver.quit()

def suite():
        s1 = unittest.TestLoader().loadTestsFromTestCase(Tests)
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


    #suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
    #unittest.TextTestRunner(verbosity=2).run(suite)
'''
import unittest
import sys

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import page
import random_test_data

user = 'admin'
password='secret'

#browsers = {"firefox": webdriver.Firefox, "ie": webdriver.Ie, "chrome": webdriver.Chrome, "safari": webdriver.Safari}

class AddressbookTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
    #    self.verificationErrors = []
    #    self.wait = WebDriverWait(self.driver, 100)
    #    self.driver.get("http://localhost/index.php")   
        #login to addressbook  
    #    self.user = 'admin' # user name login
    #    self.password = 'secret' # user password login 
    #    self.login_page = page.LoginPage(self.driver)
    #    self.login_page.login(self.user, self.password)
    #    self.login_page.click_submit()
        #random data
        # random data
    #   self.e_mail = (random_test_data.random_letters(6) + '@' + random_test_data.random_letters(5) + '.com') # generate random email
    #    self.phone_number = random_test_data.random_number(11)  # generate random phone number
    #    self.f_name = random_test_data.random_letters(6) # generate First name
    #    self.m_name = random_test_data.random_letters(5) # generate Middle name
    #    self.l_name = random_test_data.random_letters(7) # generate Last name
    
    def test_login_page(self):
         
        login_page = page.LoginPage(self)
        #self.assertTrue(login_page.is_title(), "addressbook application title doesn't match.")
        login_page.login(user, password)
        self.assertTrue(self.user, login_page.get_login) and self.assertTrue(self.password, login_page.get_password)
        self.login_page.click_submit()
    
        
    def test_navi(self): 
        #self.login_page 
        self.test_login_page()   
        page_navi = page.PageNavi(self.driver)
        page_navi.navigation()
    
    
    def test_add_new_record_and_delete_it(self): 
        #self.login_page
        self.test_login_page() # login to addressbook
        add_new_lnk = page.PageNavi(self.driver)
        add_new_lnk.add_lnk() #click on add new link 
        
        page_add_new = page.AddNew(self.driver)
        # filling Address on second page on Add new page
        page_add_new.fill_address(random_test_data.random_letters(5)) and self.assertTrue(random_test_data.random_letters(5)) # fill the address field
        page_add_new.click_next # navigate to next page
        
        # Filling user data
        page_add_new.fill_user_name(self.f_name,self.m_name,self.l_name) 
        self.assertTrue(self.f_name) and self.assertTrue(self.m_name) and self.assertTrue(self.l_name) 
        page_add_new.set_email(self.e_mail) and self.assertTrue(self.e_mail) 
        page_add_new.set_phone('+' + self.phone_number) and self.assertTrue('+' + self.phone_number)
        
        page_add_new.click_enter() 
        self.driver.implicitly_wait(10)
               
        # Search on the main page        
        main_page = page.MainPage(self.driver)
        main_page.search_element(self.phone_number) and self.assertTrue(self.phone_number)
        #self.driver.implicitly_wait(10)
        main_page.select_all_element()
        main_page.delete_bttn()
        
        main_page.accept_alert()
        
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        

if __name__ == "__main__":
    browsername = "firefox"
    if len(sys.argv) == 2:
        browsername = sys.argv[1].lower()
    browser = browsers[browsername]
    
    suite = unittest.TestLoader().loadTestsFromTestCase(AddressbookTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)'''
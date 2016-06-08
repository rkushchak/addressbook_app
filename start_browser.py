import time
import unittest
import sys
from selenium import webdriver
import tests.HTMLTestRunner
import tests.page
import tests.random_test_data
import tests.properties

browsers = {"firefox": webdriver.Firefox, "chrome": webdriver.Chrome, "safari": webdriver.Safari}

class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.set_window_size(1380, 880)
        self.driver.get(tests.properties._url)   
        ''' login to addressbook ''' 
        
        self.login_page = tests.page.LoginPage(self.driver)
        self.login_page.login(tests.properties.user, tests.properties.password)
        self.login_page.click_submit()
        
        #random data
        ''' random data'''
        self.e_mail = (tests.random_test_data.random_letters(6) + '@' + tests.random_test_data.random_letters(5) + '.com') # generate random email
        self.phone_number = tests.random_test_data.random_number(11)  # generate random phone number
        self.f_name = tests.random_test_data.random_letters(6) # generate First name
        self.m_name = tests.random_test_data.random_letters(5) # generate Middle name
        self.l_name = tests.random_test_data.random_letters(7) # generate Last name

    def test_login_page(self):
        self.login_page
        
    
    def test_navi(self): 
        self.login_page 
        #self.test_login_page()   
        page_navi = tests.page.PageNavi(self.driver)
        page_navi.navigation()
    
    def test_add_new_record_and_delete_it(self): 
        #self.login_page
        self.test_login_page # login to addressbook
        add_new_lnk = tests.page.PageNavi(self.driver)
        add_new_lnk.add_lnk() #click on add new link 
        
        page_add_new = tests.page.AddNew(self.driver)
        # filling Address on second page on Add new page
        page_add_new.fill_address(tests.random_test_data.random_letters(5)) and self.assertTrue(tests.random_test_data.random_letters(5)) # fill the address field
        page_add_new.click_next # navigate to next page
        
        # Filling user data
        page_add_new.fill_user_name(tests.properties.f_name,tests.properties.m_name,tests.properties.l_name) 
        self.assertTrue(tests.properties.f_name) and self.assertTrue(tests.properties.m_name) and self.assertTrue(tests.properties.l_name) 
        page_add_new.set_email(tests.properties.e_mail) and self.assertTrue(tests.properties.e_mail) 
        page_add_new.set_phone('+' + tests.properties.phone_number) and self.assertTrue('+' + tests.properties.phone_number)
        
        page_add_new.click_enter() 
        self.driver.implicitly_wait(10)
               
        # Search on the main page        
        main_page = tests.page.MainPage(self.driver)
        main_page.search_element(tests.properties.phone_number) and self.assertTrue(tests.properties.phone_number)
        #self.driver.implicitly_wait(10)
        main_page.select_all_element()
        main_page.delete_bttn()
        
        main_page.accept_alert()
    
    
    def tearDown(self):
        self.driver.quit()

def suite():
        s1 = unittest.TestLoader().loadTestsFromTestCase(Tests)
        return unittest.TestSuite([s1])

#This function declares the Test Results and stores them in /home/rkushchak/workspace/addressbook/tests/reports
def run(suite, report = "/home/rkushchak/workspace/addressbook/tests/reports/test_reports_%s.html" % time.asctime()):
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
    unittest.main()

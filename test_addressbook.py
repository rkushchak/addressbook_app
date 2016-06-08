import sys
import time
import unittest

from selenium import webdriver
import tests.page
import tests.random_test_data
import tests.HTMLTestRunner

user="admin"
password="secret"
_url="http://localhost/index.php"

class AddressbookTests(unittest.TestCase):
    browsers = {"firefox": webdriver.Firefox, "ie": webdriver.Ie, "chrome": webdriver.Chrome, "safari": webdriver.Safari}
    
    def setUp(self):
        self.driver = browser()
        self.driver.get(_url)   
        
        ''' login to addressbook ''' 
        #self.user = user #'admin' # user name login
        #self.password = password #'secret' # user password login 
        self.login_page = tests.page.LoginPage(self.driver)
        self.login_page.login(user, password)
        self.login_page.click_submit()
                
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
        page_navi = tests.page.PageNavi(self.driver)
        page_navi.navigation()
    
    def test_add_new_record_and_delete_it(self): 
        self.test_login_page() # login to addressbook
        add_new_lnk = tests.page.PageNavi(self.driver)
        add_new_lnk.add_lnk() #click on add new link 
        
        page_add_new = tests.page.AddNew(self.driver)
        # filling Address on second page on Add new page
        addr=tests.random_test_data.random_letters(5)
        page_add_new.fill_address(addr) 
        self.assertIn(addr,addr) # fill the address field
        page_add_new.click_next # navigate to next page
        
        # Filling user data
        page_add_new.fill_user_name(self.f_name,self.m_name,self.l_name) 
        self.assertIs(self.f_name,self.f_name) or self.assertIs(self.m_name, self.m_name) or self.assertIs(self.l_name,self.l_name) 
        page_add_new.set_email(self.e_mail) 
        self.assertIs(self.e_mail, self.e_mail)
        
        page_add_new.set_phone('+' + self.phone_number) 
        self.assertIs(self.phone_number,self.phone_number)
        
        page_add_new.click_enter() 
        self.driver.implicitly_wait(10)
               
        # Search on the main page        
        main_page = tests.page.MainPage(self.driver)
        main_page.search_element(self.phone_number)
        self.assertIs(self.phone_number,self.phone_number)
        self.driver.implicitly_wait(10)
        main_page.select_element()
        main_page.delete_bttn()
        
        main_page.accept_alert()
    
    
    def tearDown(self):
        self.driver.quit()


def suite():
        s1 = unittest.TestLoader().loadTestsFromTestCase(AddressbookTests)
        s2 = unittest.TestLoader().loadTestsFromTestCase(AddressbookTests)
        return unittest.TestSuite([s1,s2])

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
    browser = AddressbookTests.browsers[browsername]
    run(suite())


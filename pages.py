'''
Created on May 10, 2016

@author: rkushchak
'''
from locators import LoginPageLocators
from locators import PageNaviLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver
  

class LoginPage(BasePage):
    #login page 
    
    # Verifies that the hardcoded text "Addressbook" appears in page title
    def is_title(self):
        return "Address book" in self.driver.title
    # set the username
    def set_login(self, user):
        loginElement = self.driver.find_element(*LoginPageLocators.USERNAME)
        loginElement.send_keys(user)
    
    def get_login(self, user):
        return self.driver.find_element(*LoginPageLocators.USERNAME)
        
    # set the password    
    def set_password(self, password):
        passElement = self.driver.find_element(*LoginPageLocators.PASSWORD)
        passElement.send_keys(password)
    
    def get_password(self, password):
        return self.driver.find_element(*LoginPageLocators.PASSWORD)
            
    
    # Define the login button
    def click_submit(self):
        submitBttn = self.driver.find_element(*LoginPageLocators.SUBMIT)
        submitBttn.click()
        
    # login to addressbook app    
    def login(self, user, password):
        self.set_login(user)
        self.set_password(password)
        #self.click_submit()
        

class PageNavi(BasePage):
    ''' Page navigation links'''
    # Navigate to Home   
    def home_lnk(self):
        self.driver.find_element(*PageNaviLocators.HOME).click() # Find and click on "Home" link
       
    # Navigate to Add New            
    def add_lnk(self):            
        self.driver.find_element(*PageNaviLocators.ADDNEW).click() # Find and click on "add new" link
    
    # Navigate to Groups            
    def groups_lnk(self):
        self.driver.find_element(*PageNaviLocators.GROUPS).click() # Find and click on "groups" link
    
    # Navigate to Next Birthday            
    def birthdays_lnk(self):
        self.driver.find_element(*PageNaviLocators.NEXTBIRTDAY).click() # Find and click on "next birthday" link
    
    # Navigate to Print All
    def print_all_lnk(self):
        self.driver.find_element(*PageNaviLocators.PRINTALL).click()         # Find and click on "print all" link
    
    # Navigate to Print Phones
    def print_phones_lnk(self):
        self.driver.find_element(*PageNaviLocators.PRINTPHONES).click() # Find and click on "print phones" link
    
    # Navigate to Maps       
    def map_lnk(self):
        self.driver.find_element(*PageNaviLocators.MAP).click() # Find and click on "map" link
    
    # Navigate to Export
    def export_lnk(self):
        self.driver.find_element(*PageNaviLocators.EXPORT).click() # Find and click on "export" link
    
    # Navigate to Import
    def import_lnk(self):
        self.driver.find_element(*PageNaviLocators.IMPORT).click() # Find and click on "import" link
    # Logout
    def logout_lnk(self):
        self.driver.find_element(*PageNaviLocators.LOGOUT).click() # Find and click on "map" link
    
    # Smoke navigation
    def navigation(self):
            self.home_lnk()
            self.add_lnk()
            self.groups_lnk()
            self.birthdays_lnk()
            
            self.print_all_lnk()
            self.driver.back()
            self.print_phones_lnk()
            self.driver.back()
            
            self.map_lnk()
            self.export_lnk()
            self.import_lnk()
            
            self.logout_lnk()
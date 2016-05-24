from locators import LoginPageLocators, MainPageLocators, AddNewLocators


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
        self.driver.find_element(*MainPageLocators.HOME).click() # Find and click on "Home" link
       
    # Navigate to Add New            
    def add_lnk(self):            
        self.driver.find_element(*MainPageLocators.ADDNEW).click() # Find and click on "add new" link
    
    # Navigate to Groups            
    def groups_lnk(self):
        self.driver.find_element(*MainPageLocators.GROUPS).click() # Find and click on "groups" link
    
    # Navigate to Next Birthday            
    def birthdays_lnk(self):
        self.driver.find_element(*MainPageLocators.NEXTBIRTDAY).click() # Find and click on "next birthday" link
    
    # Navigate to Print All
    def print_all_lnk(self):
        self.driver.find_element(*MainPageLocators.PRINTALL).click()         # Find and click on "print all" link
    
    # Navigate to Print Phones
    def print_phones_lnk(self):
        self.driver.find_element(*MainPageLocators.PRINTPHONES).click() # Find and click on "print phones" link
    
    # Navigate to Maps       
    def map_lnk(self):
        self.driver.find_element(*MainPageLocators.MAP).click() # Find and click on "map" link
    
    # Navigate to Export
    def export_lnk(self):
        self.driver.find_element(*MainPageLocators.EXPORT).click() # Find and click on "export" link
    
    # Navigate to Import
    def import_lnk(self):
        self.driver.find_element(*MainPageLocators.IMPORT).click() # Find and click on "import" link
    # Logout
    def logout_lnk(self):
        logout = self.driver.find_element(*MainPageLocators.LOGOUT)
        logout.click() # Find and click on "map" link
    
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

class AddNew(BasePage):
    ''' Page Add New '''   
    def set_address(self, address):
        addrElement = self.driver.find_element(*AddNewLocators.ADDRESS)
        addrElement.send_keys(address)
        
    def click_next(self):
        self.driver.find_element(*AddNewLocators.NEXT).click()
            
    def fill_address(self, address):
        self.set_address(address)
        self.click_next()
        
    ''' Add New - Second Page '''
    def set_first_name(self, firstname):
        addrElement = self.driver.find_element(*AddNewLocators.FIRSTNAME)
        addrElement.clear()
        addrElement.send_keys(firstname)
    
    def set_middle_name(self, middlename):
        addrElement = self.driver.find_element(*AddNewLocators.MIDDLENAME)
        addrElement.clear()
        addrElement.send_keys(middlename)
    
    def set_last_name(self, lastname):
        addrElement = self.driver.find_element(*AddNewLocators.LASTNAME)
        addrElement.clear()
        addrElement.send_keys(lastname)
        
    """Filling random user name  etc. """
    def fill_user_name(self, firstname, middlename, lastname):
        self.set_first_name(firstname)
        self.set_middle_name(middlename)
        self.set_last_name(lastname)
    """ """
    def set_email(self, email):
        addrElement = self.driver.find_element(*AddNewLocators.EMAIL)
        addrElement.clear()
        addrElement.send_keys(email)
            
    def set_phone(self, phone):
        addrElement = self.driver.find_element(*AddNewLocators.PH_HOME)
        addrElement.clear()
        addrElement.send_keys(phone)
            
    def click_enter(self):
        next_btn = self.driver.find_element(*AddNewLocators.ENTER)
        next_btn.click()

class MainPage(BasePage):
    def search_element(self,email):
        search_elem = self.driver.find_element(*MainPageLocators.SEARCH)
        search_elem.send_keys(email)
    
    def select_element(self):
        select_elem = self.driver.find_element(*MainPageLocators.SEL_All)
        select_elem.click()
    
    def select_all_element(self):
        select_elem = self.driver.find_element(*MainPageLocators.SEL_All)
        select_elem.click()
    
    def delete_bttn(self):
        del_elem = self.driver.find_element(*MainPageLocators.DELETE)
        del_elem.click()
    
    def accept_alert(self):
        try:
            alert = self.driver.switch_to_alert()
            alert.accept()
        except:
            print "no alert to accept"

    
    
    
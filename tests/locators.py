from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    """A class for login page locators. All login page locators should come here"""
    #locators
    BASEURL = 'http://localhost:80/index.php'
    USERNAME = (By.NAME, 'user')
    PASSWORD = (By.NAME, 'pass')
    SUBMIT = (By.XPATH, './/*[@id="LoginForm"]/input[3]')
    
class MainPageLocators(object):
    """A class for main page navigation locators. All main page navigation locators should come here"""
    '''Links''' 
    HOME = (By.LINK_TEXT,'home')     #  or (By.XPATH,'.//*[@id="nav"]/ul/li[1]/a')
    ADDNEW = (By.LINK_TEXT,'add new')    #  or (By.XPATH, './/*[@id="nav"]/ul/li[2]/a')
    GROUPS  = (By.LINK_TEXT,'groups')   # or (By.XPATH,'.//*[@id="nav"]/ul/li[3]/a') 
    NEXTBIRTDAY = (By.LINK_TEXT,'next birthdays')    # or (By.XPATH,'.//*[@id="nav"]/ul/li[4]/a')  
    PRINTALL = (By.LINK_TEXT,'print all')   # or (By.XPATH,'.//*[@id="nav"]/ul/li[5]/a')  
    PRINTPHONES = (By.LINK_TEXT,'print phones') # or (By.XPATH,'.//*[@id="nav"]/ul/li[6]/a') 
    MAP = (By.LINK_TEXT,'map') # or  (By.XPATH,'.//*[@id="nav"]/ul/li[7]/a') 
    EXPORT = (By.LINK_TEXT,'export') # or (By.XPATH,'.//*[@id="nav"]/ul/li[8]/a') 
    IMPORT = (By.LINK_TEXT,'import') # or (By.XPATH,'.//*[@id="nav"]/ul/li[9]/a')
    LOGOUT = (By.LINK_TEXT, 'Logout')
    '''Buttons'''
    SEARCH = (By.NAME,'searchstring')
    SEND_EMAIL = (By.XPATH, './/*[@id="content"]/form[2]/div[1]/input')
    DELETE = (By.XPATH,'.//*[@id="content"]/form[2]/div[2]/input')
    ''' Check boxes'''
    SEL_All  = (By.XPATH,'.//*[@id="MassCB"]')
    SELECT = (By.NAME, 'selected[]')
    
    

class AddNewLocators(object):
    ADDRESS = (By.XPATH, 'id("content")/x:form/x:textarea') #'//textarea[@name="address"]')
    # Next button
    NEXT = (By.XPATH, './/*[@id="content"]/form/input[2]') # (By.NAME, 'quickadd')
    # Enter button
    ENTER = (By.NAME, 'submit')
    #Next page locators
    FIRSTNAME = (By.NAME, 'firstname') #(By.XPATH, './/*[@id="content"]/form/input[3]')
    MIDDLENAME = (By.NAME, 'middlename')
    LASTNAME = (By.NAME, 'lastname')
    NICKNAME = (By.NAME, 'nickname')
    PHOTO = (By.NAME, 'photo')
    TITLE = (By.NAME, 'title')
    COMPANY = (By.NAME, 'company')
    ADDRESS = (By.NAME, 'address')
    #Telephone
    PH_HOME = (By.NAME, 'home')
    PH_MOBILE = (By.NAME, 'mobile')
    PH_WORK = (By.NAME, 'work')
    FAX = (By.NAME, 'fax')
    #Emails
    EMAIL = (By.NAME, 'email')
    EMAIL2 = (By.NAME, 'email2')
    EMAIL3 = (By.NAME, 'email3')
    HOMEPAGE = (By.NAME, 'homepage')
    #Birthday
    BDAY = (By.NAME, 'bday')
    BYEAR = (By.NAME, 'byear')
    BMONTH = (By.NAME, 'bmonth')
    #Anniversary
    ADAY = (By.NAME, 'aday')
    AYEAR = (By.NAME, 'ayear')
    AMONTH = (By.NAME, 'amonth')
    #Group
    GROUP = (By.NAME, 'new_group')
    #Secondary
    ADDRESS2 = (By.NAME, 'address2')
    HOME = (By.NAME, 'home2')
    NOTES = (By.NAME, 'notes')

    

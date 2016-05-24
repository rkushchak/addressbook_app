'''
Created on May 10, 2016

@author: rkushchak
'''
from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    """A class for login page locators. All login page locators should come here"""
    #locators
    BASEURL = 'http://localhost:80/index.php'
    USERNAME = (By.NAME, 'user')
    PASSWORD = (By.NAME, 'pass')
    SUBMIT = (By.XPATH, './/*[@id="LoginForm"]/input[3]')
    
class PageNaviLocators(object):
    """A class for page navigation locators. All page navigation locators should come here"""
    #locators 
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


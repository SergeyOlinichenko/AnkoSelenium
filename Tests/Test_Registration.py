import pytest
from Core.CommonHelper import *
from Locators import LoginPageLocators
from Locators.LoginPageLocators import LoginPage
import xml.etree.ElementTree
from Locators.RegistrationLocators import RegisterPage
import re 
import time
 


class TestClass:
    
    
    @pytest.mark.usefixtures("driver", "url")
    def test_RegisterNewValidUser(self, driver, url):
        #Parsing data from data.xml located in Tests folder
        data = xml.etree.ElementTree.parse("data.xml")
        firstName = data.find("./firstName").text
        lastName = data.find("./lastName").text
        password = data.find("./password").text
        #Generating unique email with current epoch time
        uniqueID = str(time.time())
        uniqueID = re.sub("\.\d*", "", uniqueID)
        uniqueEmail = (uniqueID + "@testmail.com")
        #Navigating to URL from command line
        driver.get(url)
        #Waiting for page loading and click on Join Now link
        waitAndClick(driver, LoginPage.registerLink)
        #Click on "join using your Email Address" button
        waitAndClick(driver, RegisterPage.register)
        #Adding data to text fields
        waitAndInputText(driver, RegisterPage.firstName, firstName)
        waitAndInputText(driver, RegisterPage.secondName, lastName)
        waitAndInputText(driver, RegisterPage.email, uniqueEmail)
        waitAndInputText(driver, RegisterPage.password, password)
        #Click on Join Now button
        waitAndClick(driver, RegisterPage.registerButton)
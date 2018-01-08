from selenium.webdriver.common.by import By

class RegisterPage():
    register = (By.XPATH, "//a[@uisref='join-now']")
    firstName = (By.NAME, "FirstName")
    secondName = (By.NAME, "LastName")
    email = (By.NAME, "UserName")
    password = (By.NAME, "Password")
    registerButton = (By.XPATH, "//button[contains(., 'Join Now')]")
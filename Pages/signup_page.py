from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class signUpPage:


    def __init__(self, driver):
        self.driver = driver
        self.tap_signup = (By.XPATH, "//*[@id='__next']/div/main/nav/div[4]/ul[2]/li[2]/a/button")
        self.fullName = (By.NAME, "name")
        self.email = (By.NAME, "email")
        self.phoneNumber = (By.NAME, "phone_number")
        self.business_name = (By.NAME, "business_name")
        self.rc_number = (By.NAME, "rc_number")
        self.password = (By.NAME, "password")
        self.continue_button = (By.XPATH, "//*[@id='hide-flow-tag']/div/div/div/div/div/div/form/button")

    # Open a URL
    def open_page(self, url):
        self.driver.get(url)

    # Enter Fullname (Takes full name)
    def enter_fullname(self, fullName):
        user = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.fullName))
        user.send_keys(fullName)

    # Enter Business name
    def enter_businessName(self, businessName):
        user = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.business_name))
        user.send_keys(businessName)

    # Enter Email (Takes Email)
    def enter_email(self, email):
        user = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.email))
        user.send_keys(email)

    # Enter Phone number (Takes Phone number)
    def enter_phoneNumber(self, phoneNumber):
        user = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.phoneNumber))
        user.send_keys(phoneNumber)

    # Enter Phone number (Takes Phone number)
    def enter_rcNumber(self, rcNumber):
        user = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.rc_number))
        user.send_keys(rcNumber)

    #   Enter Password (Takes Password)
    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    # Click the Continue button
    def click_continue(self):
        continue_click = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.continue_button))
        continue_click.click()
    

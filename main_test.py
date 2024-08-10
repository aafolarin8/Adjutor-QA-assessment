import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from Pages.signup_page import signUpPage
from Pages.login_page import LoginPage
import random
import unittest
from faker import Faker

def driver():
    chromedriver_path = 'C:/Users/Olande/Desktop/Lendsqr/chromedriver.exe'
    
    # Create a Service object (recommended)
    service = Service(executable_path = chromedriver_path)
    service.start()

    
    chrome_options = Options()
    # chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    # chrome_options.add_argument('--headless')

    # Create the WebDriver instance
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()

    # Return the driver
    return driver

def signup(driver):
    signup_page = signUpPage(driver)
    fake = Faker()

    signup_page.open_page("https://app.adjutor.io/signup")
    signup_page.enter_fullname(fake.name())
    signup_page.enter_email("afola@mailinator.com")
    signup_page.enter_phoneNumber(fake.phone_number())
    signup_page.enter_businessName("Capitalism")
    signup_page.enter_rcNumber('RC1234567890')
    signup_page.enter_password("Pa$$w0rd!")
    time.sleep(1)
    signup_page.click_continue()


def login(driver):
    login_page = LoginPage(driver)
    fake = Faker()

    login_page.open_page("https://app.adjutor.io/login")
    login_page.enter_email("afolarinn8@gmail.com")
    login_page.enter_password("Pa$$w0rd!")
    login_page.click_login()





def test(driver):
    #Initialize the Page Classes
    login(driver)
    # signup(driver)

    
    time.sleep(10)


test(driver()) # Call Start Function
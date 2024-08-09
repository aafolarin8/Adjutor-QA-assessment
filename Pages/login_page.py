from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    # Initialize Class with locators and variables 
    def __init__(self, driver):
        self.driver = driver
        self.tap_login = (By.CSS_SELECTOR, "#__next > div > main > nav > div.styles_nav_container__tjwJl > ul.styles_right__o6MBb > li:nth-child(1) > a > button")
        self.email = (By.NAME, "email")  #   Email address 
        self.password = (By.NAME, "password")  # Password
        self.login_button = (By.XPATH, "//*[@id='hide-flow-tag']/div/div[1]/form/button")  # Login Button
        
    # Open a URL
    def open_page(self, url):
        self.driver.get(url)

    # Enter Email (Takes Email)
    def enter_email(self, email):
        user = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.email))
        user.send_keys(email)

    #   Enter Password (Takes Password)
    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    # Click Login Button
    def click_login(self):
        login_click = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button))
        login_click.click()

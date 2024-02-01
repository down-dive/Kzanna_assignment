from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from .common import CommonOps
from selenium.webdriver.common.keys import Keys


class FormAuthentication(CommonOps):
    
    # Locators for elements on the Form Authentication page
    LOGIN_EMAIL_INPUT = (By.ID, "basic_email")
    LOGIN_PASSWORD_INPUT = (By.ID, "basic_password")
    SIGN_IN_BUTTON = (By.XPATH, '//button[text()="Sign In"]')
    # LOGIN_ERROR_MESSAGE = (By.XPATH, '//span[contains(text(),"this account has been temporarily disabled")]')
    LOGIN_ERROR_MESSAGE = (By.XPATH, '//div[contains(@class, "message-error")]')
    DASHBOARD_MENU_ITEM = (By.XPATH, "//span[text()='Dashboard']")
    IFRAME = (By.XPATH, '//iframe[@class="full-screen-preview__frame"]')

    # Enter the username in the login email input field
    def enter_login_username(self, username):
        self.wait_for(self.LOGIN_EMAIL_INPUT).click()
        self.find(self.LOGIN_EMAIL_INPUT).send_keys(Keys.COMMAND + "a", Keys.DELETE)         
        time.sleep(1)
        self.find(self.LOGIN_EMAIL_INPUT).send_keys(username, Keys.TAB)

    # Enter the password in the login password input field
    def enter_login_password(self, password):
        self.wait_for(self.LOGIN_PASSWORD_INPUT).click()
        self.find(self.LOGIN_PASSWORD_INPUT).send_keys(Keys.COMMAND + "a", Keys.DELETE)
        self.find(self.LOGIN_PASSWORD_INPUT).send_keys(password)

    # Click the Sign In button
    def click_login_button(self):
        time.sleep(1)
        self.find(self.SIGN_IN_BUTTON).click()
        time.sleep(1)

    # Perform the login action by entering username and password and clicking the Sign In button
    def login(self, username, password):
        self.enter_login_username(username)
        self.enter_login_password(password)
        self.click_login_button()
        time.sleep(2)
    
    # Check if the login error message is displayed
    def login_error(self):
        return self.find(self.LOGIN_ERROR_MESSAGE).is_displayed()
    
    # Check if the Dashboard menu item is displayed, indicating a successful login
    def login_success(self):
        return self.find(self.DASHBOARD_MENU_ITEM).is_displayed()
    


        
        
        
        
        
        
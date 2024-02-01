from selenium.webdriver.common.by import By
import time
import requests

from .common import CommonOps

class DashboardCrm(CommonOps):
    
    # Locators for elements on the DashboardCrm page
    DASHBOARD_IFRAME = (By.XPATH, "//iframe[contains(@class, 'frame')]")
    DASHBOARD_MENU_ITEM = (By.XPATH, "//span[text()='Dashboard']")
    CRM_MENU_ITEM = (By.XPATH, "//a[@href='/main/dashboard/crm']")
    MAIL_APP_MENU_ITEM = (By.XPATH, "//a[@href='/in-built-apps/mail']")
    TOTAL_REVENUE_VALUE = (By.XPATH, '//h1[contains(@class, "revenue-title")]')
    COMPOSE_BUTTON = (By.XPATH, '//button[contains(text(), "COMPOSE")]')
    MAIL_TO_INPUT = (By.XPATH, '//input[@placeholder="To*"]')
    MAIL_SUBJECT_INPUT = (By.XPATH, '//input[@placeholder="Subject"]')
    MAIL_MESSAGE_INPUT = (By.XPATH, '//textarea[@placeholder="Message"]')
    ATTACH_FILE_BUTTON = (By.XPATH, '//span[text()=" Attach File"]')
    MAIL_SEND_BUTTON = (By.XPATH, '//span[text()="OK"]')
    MAIL_SENT_ALERT = (By.ID, "message-id")

    # Sample data for composing mail
    recepient_email = 'smaple@company.com'
    subject_text = 'Something'
    message_text = ' A new test Message'
    attachment_file_path = './xyz'
    api_url = "https://jsonplaceholder.typicode.com/posts/"

    # Navigate to the Dashboard page   
    def go_to_dashboard(self):
        self.wait_for_clickable(self.DASHBOARD_MENU_ITEM).click()
    
    # Navigate to the CRM page            
    def go_to_crm(self):
        self.wait_for_clickable(self.CRM_MENU_ITEM).click()
     
    # Get the total revenue value from the page    
    def get_revenue_value(self):
        return self.find(self.TOTAL_REVENUE_VALUE).text
    
    # Navigate to the Mail App page    
    def go_to_mail_app(self):
        self.wait_for_clickable(self.MAIL_APP_MENU_ITEM).click()
    
    # Compose a new mail by filling in recipient, subject, and message fields    
    def compose_mail(self):
        self.wait_for_clickable(self.COMPOSE_BUTTON).click()
        time.sleep(2)
        self.find(self.MAIL_TO_INPUT).send_keys(self.recepient_email)
        self.find(self.MAIL_SUBJECT_INPUT).send_keys(self.subject_text)
        self.find(self.MAIL_MESSAGE_INPUT).send_keys(self.message_text)

    # Attach a file, send mail, and wait for the mail sent alert
    def attach_file_and_send(self):
        # self.attach_file(self.attachment_file_path)
        files = {'file': ('test_text_file', open(self.attachment_file_path, 'rb'), 'application/octet-stream')}
        headers = {
        'Authorization': 'authorization-text',  # Add any other necessary headers
        'Referer': 'https://wieldy.g-axon.work',  # Add the correct referer
        }
        time.sleep(5)
        response = requests.post(self.api_url, files=files, headers=headers)
        time.sleep(2)
        self.wait_for_clickable(self.MAIL_SEND_BUTTON).click()
        time.sleep(1)
        return self.find(self.MAIL_SENT_ALERT).is_displayed()
     
    # Check and return the mail sent alert message   
    def check_mail_sent_message(self):
        return self.wait_for(self.MAIL_SENT_ALERT)
        

from selenium import webdriver
import pytest
import time

# Fixture to create a WebDriver instance for testing
@pytest.fixture
def driver():
    # URL for the initial page before switching to the iframe
    given_url = "https://preview.themeforest.net/item/wieldy-react-redux-ant-design-admin-template/full_screen_preview/22719616?_ga=2.62160101.837904251.1706544053-1484721041.1706544053"
    
    # URL of the iframe that you navigate to initially
    iframe_url = "https://wieldy.g-axon.work/"
    # Create a Chrome WebDriver instance, to use Firefox instance comment the code bellow and uncomment Firefox driver
    driver = webdriver.Chrome(executable_path='drivers/chromedrivermac')
    # driver = driver.Firefox(executable_path='drivers/geckodriver')
    
    # Navigate to the iframe URL
    driver.get(iframe_url)
    
     # Wait for 2 seconds (adjust as needed)
    time.sleep(2)
    
    # Yield the WebDriver instance to the test function
    yield driver
    
    # Close the WebDriver instance after the test is complete
    driver.close()
    
    
    


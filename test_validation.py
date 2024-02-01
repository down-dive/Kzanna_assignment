import pytest
from pages.formAuth import FormAuthentication
from pages.dashboard import DashboardCrm
import time

# Test data
valid_username = 'demo@example.com'
valid_password = 'demo#123'
invalid_username = 'demo1@company.com'
invalid_password = '123456'

# Fixture to log in and return FormAuthentication instance
@pytest.fixture
def logged_in_form(driver):
    form = FormAuthentication(driver)
    form.login(valid_username, valid_password)
    return form

# Test for invalid authentication
def test_invalid_authentication(driver):
    form = FormAuthentication(driver)
    form.login(invalid_username, invalid_password)
    assert form.login_error(), "Error message did not show up"

# Test for valid authentication using the logged_in_form fixture
def test_valid_authentication(logged_in_form):
    assert logged_in_form.login_success(), "Login unsuccessful"

# Test CRM dashboard functionality
def test_crm_dashboard(logged_in_form, driver):
    dashboard = DashboardCrm(driver)
    
    # Navigate to CRM dashboard
    dashboard.go_to_dashboard()
    dashboard.go_to_crm()
    
    # Wait for 5 seconds (adjust as needed)
    time.sleep(5)
    
     # Get and assert revenue value
    revenue_value = int(dashboard.get_revenue_value().replace('$', '').replace(',', ''))
    print("Revenue value:", revenue_value)
    assert revenue_value > 0, "No revenue value"

# Test apps dashboard functionality
def test_apps_dashboard(logged_in_form, driver):
    dashboard = DashboardCrm(driver)
    
    # Navigate to mail app and perform actions
    dashboard.go_to_mail_app()
    dashboard.compose_mail()
    
    
    # Assert the success message
    assert dashboard.attach_file_and_send(), "Sending message failed"

# Open https://the-internet.herokuapp.com/login

# Please automate next test cases:


# 3. Logout from app and assert you successfully logged out

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

VALID_CREDS = {'username_t01': 'tomsmith',
               'password_t01': 'SuperSecretPassword!' }

INVALID_CREDS = {'username_nrt01': 'test123',
                 'password_nrt01': 'testpass' }

url = 'https://the-internet.herokuapp.com/login'

#1.Login with valid creds/Logout from app (tomsmith / SuperSecretPassword!) and assert you successfully logged in

driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(VALID_CREDS['username_t01'])
driver.find_element(By.CSS_SELECTOR, "#password").send_keys(VALID_CREDS['password_t01'])
driver.find_element(By.CSS_SELECTOR, ".fa").click()
time.sleep(2)
assert 'Welcome to the Secure Area' in driver.page_source
print('Login with valid creds is OK!' )
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".button").click()
assert 'Login Page' in driver.page_source
print('Logout is OK!')
driver.quit()

# 2. Login with invalid creds and check validation error

driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(INVALID_CREDS['username_nrt01'])
driver.find_element(By.CSS_SELECTOR, "#password").send_keys(INVALID_CREDS['password_nrt01'])
driver.find_element(By.CSS_SELECTOR, ".fa").click()
time.sleep(3)
assert 'Your username is invalid!' in driver.page_source
print('Login with invalid creds is OK!(Validation message is shown)' )
driver.quit()

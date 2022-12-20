import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Open browser
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(2)

# Go to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)

# Type username student into Username field
username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")

# Type password Password123 into Password field
password_locator = driver.find_element(By.ID, "password")
password_locator.send_keys("Password123")

# Puch Submit button
submit_button_locator = driver.find_element(By.ID, "submit")
submit_button_locator.click()

# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
page_url_locator = driver.find_element(By.XPATH, "//head//link[@rel='canonical']")
obtained_url_text = page_url_locator.get_attribute("href")
expected_url_text = "practicetestautomation.com/logged-in-successfully/"

if expected_url_text in obtained_url_text:
    print("The new page URL contains " + expected_url_text)
else:
    print("The new page URL does not contain " + expected_url_text)

# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
article_locator = driver.find_element(By.TAG_NAME, "article")
article_text = article_locator.text
expected_phrases = ["Congratulations", "successfully logged in"]

result = (phrase for phrase in expected_phrases if phrase in article_text)

for res in result:
    print(f"'{res}' is visible in new page")

# Verify button Log out is displayed on the new page
logout_button_locator = driver.find_element(By.XPATH, "//div[@class='wp-block-button aligncenter is-style-fill']//a")

print('Button visible') if logout_button_locator else print('Button not visible')
    


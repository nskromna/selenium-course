import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import pytest

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
def test_new_page_contains_URL():
    page_url_locator = driver.find_element(By.XPATH, "//head//link[@rel='canonical']")
    obtained_url_text = page_url_locator.get_attribute("href")
    expected_url_text = "practicetestautomation.com/logged-in-successfully/"

    assert expected_url_text in obtained_url_text

# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
def test_new_page_contains_text():
    article_locator = driver.find_element(By.TAG_NAME, "article")
    article_text = article_locator.text
    expected_phrases = ["Congratulations", "successfully logged in"]

    result = [True for phrase in expected_phrases if phrase in article_text]

    assert result[0] & result[1]

# Verify button Log out is displayed on the new page
def test_button_is_visible():
    logout_button_locator = driver.find_element(By.XPATH, "//div[@class='wp-block-button aligncenter is-style-fill']//a")

    assert logout_button_locator
    


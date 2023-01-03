import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_username(self):
        # Open page
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorrectUser")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys("Password123")

        # Puch Submit button
        submit_button_locator = driver.find_element(By.ID, "submit")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_msg_locator = driver.find_element(By.ID, "error")
        assert error_msg_locator.is_displayed(), "Error message is not displayed, but it should be"

        # Verify error message text is Your username is invalid!
        error_msg = error_msg_locator.text
        assert error_msg == "Your username is invalid!", "Error message is different to expected"
    

    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_password(self):
        # Open page
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type password incorrectPassword into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys("incorrectPassword")

        # Puch Submit button
        submit_button_locator = driver.find_element(By.ID, "submit")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_msg_locator = driver.find_element(By.ID, "error")
        assert error_msg_locator.is_displayed(), "Error message is not displayed, but it should be"

        # Verify error message text is Your password is invalid!
        error_msg = error_msg_locator.text
        assert error_msg == "Your password is invalid!", "Error message is different to expected"
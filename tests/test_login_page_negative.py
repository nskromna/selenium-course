import time

import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message", [("incorrectUser", "Password123", "Your username is invalid!"), ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys(password)

        # Puch Submit button
        submit_button_locator = driver.find_element(By.ID, "submit")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_msg_locator = driver.find_element(By.ID, "error")
        assert error_msg_locator.is_displayed(
        ), "Error message is not displayed, but it should be"

        # Verify error message text is Your username is invalid!
        error_msg = error_msg_locator.text
        assert error_msg == expected_error_message, "Error message is different to expected"

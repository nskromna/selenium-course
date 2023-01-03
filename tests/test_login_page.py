import time

import pytest
from selenium.webdriver.common.by import By


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):

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
        current_url_text = driver.current_url
        expected_url_text = "https://practicetestautomation.com/logged-in-successfully/"

        assert current_url_text == expected_url_text

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        article_locator = driver.find_element(By.TAG_NAME, "article")
        article_text = article_locator.text
        expected_phrases = ["Congratulations", "successfully logged in"]

        result = [phrase for phrase in expected_phrases if phrase in article_text]

        assert result[0] or result[1]

        # Verify button Log out is displayed on the new page
        logout_button_locator = driver.find_element(
            By.XPATH, "//div[@class='wp-block-button aligncenter is-style-fill']//a")

        assert logout_button_locator
        # print('Button visible') if logout_button_locator else print('Button not visible')

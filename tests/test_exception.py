import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):

        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        add_btn_locator = driver.find_element(By.ID, "add_btn")
        add_btn_locator.click()

        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(ec.presence_of_element_located(
            (By.XPATH, "//div[@id='row2']//input")))

        assert row_2_input_element.is_displayed(
        ), "Input in row 2 should be displayed but it is not"

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):

        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_btn_locator = driver.find_element(By.ID, "add_btn")
        add_btn_locator.click()

        # Wait for the second row to load
        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(ec.presence_of_element_located(
            (By.XPATH, "//div[@id='row2']//input")))

        # Type text into the second input field
        row_2_input_element.send_keys("Spaghetti")

        # Push Save button using locator By.name(“Save”)
        save_btn_locator = driver.find_element(
            By.XPATH, "//div[@id='row2']//button[@name='Save']")
        save_btn_locator.click()

        # Verify text saved
        confirmation_msg_element = wait.until(ec.visibility_of_element_located(
            (By.XPATH, "//div[text()='Row 2 was saved']")))
        assert confirmation_msg_element, "Confirmation message should be visible, but is not"

    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):

        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Clear input field
        driver.find_element(By.ID, "edit_btn").click()
        row_1_input_locator = driver.find_element(
            By.XPATH, "//div[@id='row1']//input")
        row_1_input_locator.clear()

        # Type text into the input field
        row_1_input_locator.send_keys("Spaghetti")
        save_btn_locator = driver.find_element(
            By.XPATH, "//div[@id='row1']//button[@name='Save']")
        save_btn_locator.click()

        # Verify text changed
        assert row_1_input_locator.get_attribute("value") == "Spaghetti"

    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self, driver):

        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Push add button
        add_btn_locator = driver.find_element(By.ID, "add_btn")
        add_btn_locator.click()

        # Verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located(
            (By.ID, "instructions")), "Instruction text element is displayed and should not be.")
    
    @pytest.mark.exceptions
    def test_timeout_exception(self, driver):

        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Push add button
        add_btn_locator = driver.find_element(By.ID, "add_btn")
        add_btn_locator.click()

        # Wait for 3 seconds for the second input field to be displayed
        wait = WebDriverWait(driver, 6)
        
         # Verify second input field is displayed
        assert wait.until(ec.visibility_of_element_located(
            (By.XPATH, "//div[@id='row2']//input")), "Second input field is not displayed and should be")

       

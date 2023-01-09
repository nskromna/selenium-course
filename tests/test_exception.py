import pytest
from selenium.webdriver.common.by import By


class TestExceptions:

    @pytest.mark.positive
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):

        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        add_btn_locator = driver.find_element(By.ID, "add_btn")
        add_btn_locator.click()

        row_2_input_locator = driver.find_element(
            By.XPATH, "//div[@id='row2']//input")

        assert row_2_input_locator.is_displayed(
        ), "Input in row 2 should be displayed but it is not"

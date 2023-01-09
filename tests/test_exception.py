import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestExceptions:

    @pytest.mark.positive
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

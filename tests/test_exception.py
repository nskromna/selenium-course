import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.exception_page import ExceptionPage


class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.add_new_row(2)
        assert exception_page.is_row_input_displayed(2) , "Input in row 2 should be displayed but it is not"

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.add_new_row(2)
        exception_page.type_and_save_new_row("Spaghetti", 2)
        assert exception_page.get_confirmation_message() == "Row 2 was saved", "Confirmation message is not as expected"

    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.clear_input_field(1)
        exception_page.type_and_save_new_row("Spaghetti", 1)
        assert exception_page.get_input_value(1) == "Spaghetti"

    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.add_new_row(2)
        assert not exception_page.is_instruction_message_displayed(), "Instruction text element is displayed and should not be."

    @pytest.mark.exceptions
    def test_timeout_exception(self, driver):
        exception_page = ExceptionPage(driver)
        exception_page.open()
        exception_page.add_new_row(2)
        assert exception_page.is_row_input_displayed(2) , "Input in row 2 should be displayed but it is not"

       

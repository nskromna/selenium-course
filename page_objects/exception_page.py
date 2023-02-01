from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class ExceptionPage(BasePage):

    __url = "https://practicetestautomation.com/practice-test-exceptions/"

    __add_button_locator = (By.ID, "add_btn")
    __save_button_locators = [(By.XPATH, f"//div[@id='row{i}']//button[@name='Save']") for i in range(1,3)]
    __edit_button_locator = (By.ID, "edit_btn")

    __row_input_locators = [(By.XPATH, f"//div[@id='row{i}']//input") for i in range(1,3)]
    __confirmation_message_locator =  (By.ID, "confirmation")
    __instruction_message_locator = (By.ID, "instructions")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def add_new_row(self, num_of_row: int):
        super()._click(self.__add_button_locator)
        super()._wait_until_element_is_visible(self.__row_input_locators[num_of_row-1])

    def is_row_input_displayed(self, num_of_row: int) -> bool:      
        return super()._is_displayed(self.__row_input_locators[num_of_row-1])

    def type_and_save_new_row(self, text: str, num_of_row: int):
        super()._type(self.__row_input_locators[num_of_row-1], text, 3)
        super()._click(self.__save_button_locators[num_of_row-1], 3)
        super()._wait_until_element_is_visible(self.__confirmation_message_locator, 3)

    def get_confirmation_message(self) -> str:
        return super()._get_text(self.__confirmation_message_locator, 3)
    
    def is_instruction_message_displayed(self) -> bool:
        return super()._is_displayed(self.__instruction_message_locator)
    
    def clear_input_field(self, num_of_row: int):
        super()._click(self.__edit_button_locator, 3)
        super()._clear(self.__row_input_locators[num_of_row-1])
    
    def get_input_value(self, num_of_row) -> str:
        return super()._get_value_attribute(self.__row_input_locators[num_of_row-1])


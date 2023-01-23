from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoggedInSuccesfullyPage:
    _url = "https://practicetestautomation.com/logged-in-succesfully/"
    __header_locator = (By.TAG_NAME, "article")
    __logout_button = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def expected_url(self) -> str:
        return self._url

    @property
    def header(self) -> str:
        return self._driver.find_element(self.__header_locator).text

    def is_logout_buttonn_displayed(self) -> bool:
        return self._driver.find_element(self.__logout_button).is_displayed()

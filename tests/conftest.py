
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    print("Openinig Chrome driver")
    my_driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    yield my_driver
    print("Closing Chrome driver")
    my_driver.quit()

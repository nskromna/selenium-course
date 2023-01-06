import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture() #(params=["chrome", "firefox"])
def driver(request):
    browser = request.config.getoption("--browser") #request.param
    print(f"Openinig {browser} driver")

    if browser == "chrome":
        my_driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        install_dir = "/snap/firefox/current/usr/lib/firefox"
        driver_loc = os.path.join(install_dir, "geckodriver")
        binary_loc = os.path.join(install_dir, "firefox")

        service = FirefoxService(driver_loc)
        opts = webdriver.FirefoxOptions()
        opts.binary_location = binary_loc
        my_driver = webdriver.Firefox(service=service, options=opts)
        # my_driver = webdriver.Firefox(
        #     service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox' but got {browser}")

    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )

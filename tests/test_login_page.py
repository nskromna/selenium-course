import pytest

from page_objects.login_page import LoginPage
from page_objects.logged_in_successfully import LoggedInSuccesfullyPage


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("student", "Password123")
        logged_in_page = LoggedInSuccesfullyPage(driver)
        assert logged_in_page.expected_url == logged_in_page.current_url, "Current URL is not the same as expected"
        assert logged_in_page.header == 'Logged In Successfully', "Header does not contain desired phrase"
        assert logged_in_page.is_logout_button_displayed(), "Log out button is not displayed"

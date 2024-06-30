import pytest
from faker import Faker
from utils.webdriver import get_driver
from pages.login_page import LoginPage

fake = Faker()

@pytest.fixture(scope="module")
def setup():
    driver = get_driver()
    yield driver
    driver.quit()

def test_positive_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.load()

    login_page.login("student", "Password123")
    login_page.wait_for_login_success()

    assert "Congratulations" in driver.page_source or "successfully logged in" in driver.page_source
    assert login_page.is_logout_button_displayed()

def test_negative_login_invalid_username(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.load()

    invalid_username = fake.user_name()

    login_page.login(invalid_username, "Password123")

    error_message = "Your username is invalid!"
    assert error_message in driver.page_source

if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])

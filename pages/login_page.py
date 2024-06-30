from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://practicetestautomation.com/practice-test-login/"

        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.submit_button = (By.ID, "submit")
        self.logout_button = (By.ID, "logout")

    def load(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.submit_button).click()

    def wait_for_login_success(self):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(
                "practicetestautomation.com/logged-in-successfully/"))

    def is_logout_button_displayed(self):
        return self.driver.find_element(*self.logout_button).is_displayed()

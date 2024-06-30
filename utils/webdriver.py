import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_driver():
    chromedriver_path = os.getenv('CHROMEDRIVER_PATH')

    if chromedriver_path is None:
        raise ValueError("CHROMEDRIVER_PATH environment variable is not set")
    driver = webdriver.Chrome(service=Service(
        executable_path=chromedriver_path))
    driver.maximize_window()
    return driver

import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_width = 1200
    browser.config.window_height = 720
    browser.config.base_url = 'https://github.com'
    driver_options = webdriver.ChromeOptions()
    browser.config.driver_options = driver_options

    yield

    browser.quit()

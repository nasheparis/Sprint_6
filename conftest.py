import pytest
from selenium import webdriver

from data import WEBSITE


@pytest.fixture(scope='function')
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--windows-size=1920,1080')
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(WEBSITE)
    yield driver
    driver.quit()

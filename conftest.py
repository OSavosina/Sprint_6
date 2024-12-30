import pytest
from selenium import webdriver
from constants import PageUrl

base_url = PageUrl.MAIN_PAGE

@pytest.fixture()
def driver():
    browser = webdriver.Firefox()
    browser.get(base_url)
    yield browser
    browser.quit()


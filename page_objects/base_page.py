from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_page(self, url):
        self.driver.get(url)

    def find_element_base(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not find element {locator}')

    def wait_page_base(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.url_contains(locator),message=f'Not find element {locator}')

    def execute_script_base(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_current_url(self):
        return self.driver.current_url

    def page_reload(self):
        return self.driver.refresh()

    def get_cookies(self, name):
        return self.driver.get_cookie(name).values()

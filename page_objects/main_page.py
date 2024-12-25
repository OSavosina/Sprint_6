from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class MainPage:
    locator_button_get_cookies = (By.XPATH, '//button[@id="rcc-confirm-button"]')
    locator_top_button = (By.XPATH, '//button[@class="Button_Button__ra12g"]')
    locator_bottom_button = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    locator_logo_scooter = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')
    locator_logo_yandex = (By.XPATH, '//a[@href="//yandex.ru"]')


    def __init__(self, driver):
        self.driver = driver

    @allure.step('Принятие кук')
    def get_cookies(self):
        self.driver.find_element(*self.locator_button_get_cookies).click()

    @allure.step('Клик по кнопке заказать')
    def click_button_order(self, data_url):
        self.driver.find_element(*data_url).click()

    @allure.step('Клик по лого с Самокатом')
    def click_logo_scooter(self):
        self.driver.find_element(*self.locator_logo_scooter).click()

    @allure.step('Клик по лого Яндекса')
    def click_logo_yandex(self):
        self.driver.find_element(*self.locator_logo_yandex).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.url_contains('dzen.ru'))



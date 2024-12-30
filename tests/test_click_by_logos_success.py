import allure
import pytest
from locators import Locators
from page_objects.main_page import MainPage
from constants import PageUrl
from conftest import driver

class TestClickButtonsOnMainPageSuccess:
    @allure.title('Клик по кнопке принятия кук')
    def test_click_button_cookie(self, driver):
        main_page = MainPage(driver)
        assert main_page.accept_cookies() == True

    @allure.title('Клик по кнопкам Заказать')
    @pytest.mark.parametrize('locator_button', [Locators.locator_top_button, Locators.locator_bottom_button])
    def test_click_by_buttons_order(self, driver, locator_button):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        if locator_button == Locators.locator_bottom_button:
            main_page.execute_script_base()
        main_page.click_button_order(locator_button)
        assert main_page.get_current_url() == PageUrl.ORDER_PAGE

    @allure.title('Клик по лого с Самокатом')
    def test_click_by_logo_scooter_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_logo_scooter()
        assert main_page.get_current_url() == PageUrl.LOGO_SCOOTER_URL

    @allure.title('Клик по лого с Яндекс')
    def test_click_by_logo_yandex_success(self, driver):
        main_page = MainPage(driver)
        assert main_page.get_current_url() == PageUrl.LOGO_YANDEX_URL
        

from page_objects.main_page import MainPage
from constants import PageUrl
from conftest import driver

class TestClickByLogoScooterSuccess:
    def test_click_by_logo_scooter_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_logo_scooter()
        assert driver.current_url == PageUrl.LOGO_SCOOTER_URL

    def test_click_by_logo_yandex_success(self, driver):
        main_page = MainPage(driver)
        main_page.click_logo_yandex()
        assert driver.current_url == PageUrl.LOGO_YANDEX_URL
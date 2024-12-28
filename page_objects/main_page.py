from selenium.webdriver.common.by import By
from conftest import driver
from constants import PageUrl, CookieName
from page_objects.base_page import BasePage
from data import AccordionConstants
from locators import Locators
import allure


class MainPage(BasePage):
    locators_dict_accordion_heading = {}
    locators_dict_accordion_panels = {}

    def __init__(self, driver):
        super().__init__(driver)
        self.factory_locators_accordion()


    @allure.step('Фабрика локаторов для аккордиона')
    def factory_locators_accordion(self):
        for item_id in range(AccordionConstants.ACCORDION_HEADING_COUNT):
            heading = (By.XPATH, f"//div[@id='{AccordionConstants.ACCORDION_HEADING_LOCATOR}-{item_id}']/parent::*")
            self.locators_dict_accordion_heading[f"ACCORDION_HEADING_{item_id}"] = heading

            panel = (By.XPATH, f"//div[@id='{AccordionConstants.ACCORDION_PANELS_LOCATOR}-{item_id}']/p")
            self.locators_dict_accordion_panels[f"ACCORDION_PANEL_{item_id}"] = panel

    @allure.step('Открытие ответа на вопрос из списка')
    def check_accordion_panel_is_enabled(self, item_id):
        self.execute_script_base()
        self.find_element_base(locator=self.locators_dict_accordion_heading[f"ACCORDION_HEADING_{item_id}"], time=5)
        self.find_element_base(locator=self.locators_dict_accordion_heading[f"ACCORDION_HEADING_{item_id}"], time=5).click()

        return self.find_element_base(locator=self.locators_dict_accordion_panels[f"ACCORDION_PANEL_{item_id}"], time=5).text



    @allure.step('Принятие кук')
    def accept_cookies(self):
        button = self.find_element_base(locator=Locators.locator_button_get_cookies, time=2)
        button.click()
        self.page_reload()
        self.go_to_page(PageUrl.MAIN_PAGE)
        return CookieName.CARTOSHKA in self.get_cookies(CookieName.CARTOSHKA)

    @allure.step('Клик по кнопке заказать')
    def click_button_order(self, locator_button):
        button_order = self.find_element_base(locator_button, time=5)
        button_order.click()
        return self.get_current_url()

    @allure.step('Клик по лого с Самокатом')
    def click_logo_scooter(self):
        self.find_element_base(locator=Locators.locator_logo_scooter, time=5).click()
        return self.get_current_url()

    @allure.step('Клик по лого Яндекса')
    def click_logo_yandex(self):
        self.find_element_base(locator=Locators.locator_logo_yandex, time=5).click()
        self.wait_page_base('dzen.ru', 10)
        return self.get_current_url()





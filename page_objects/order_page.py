from page_objects.base_page import BasePage
from locators import Locators
import allure


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполнение формы юзера')
    def complete_user_form(self, data):
        self.find_element_base(locator=Locators.locator_input_first_name_form_order, time=2).send_keys(data['first_name'])
        self.find_element_base(locator=Locators.locator_input_second_name_form_order, time=2).send_keys(data['second_name'])
        self.find_element_base(locator=Locators.locator_input_address_form_order, time=2).send_keys(data['address'])
        self.find_element_base(locator=Locators.locator_input_metro_station_form_order, time=2).click()
        self.find_element_base(locator=Locators.locator_input_choose_metro_station_form_order, time=2).click()
        self.find_element_base(locator=Locators.locator_input_phone_number_form_order, time=2).send_keys(data['phone_number'])
        self.find_element_base(locator=Locators.locator_button_next_form_order, time=2).click()

    @allure.step('Заполнение формы заказа')
    def complete_order_form(self, data):
        self.find_element_base(locator=Locators.locator_select_date_order, time=2).click()
        self.find_element_base(locator=Locators.locator_option_date_order, time=2).click()
        self.find_element_base(locator=Locators.locator_select_period_order, time=2).click()
        self.find_element_base(locator=Locators.locator_option_period_order, time=2).click()
        self.find_element_base(locator=Locators.locator_color_order, time=2).click()
        self.find_element_base(locator=Locators.locator_input_comment, time=2).send_keys(data['order_comment'])
        self.find_element_base(locator=Locators.locator_button_make_order, time=2).click()

    @allure.step('Открытие формы подтверждения заказа')
    def confirm_order(self):
        self.find_element_base(locator=Locators.locator_button_yes, time=2).click()

    @allure.step('Запуск методов оформления заказа')
    def make_order(self, data):
        self.complete_user_form(data)
        self.complete_order_form(data)
        self.confirm_order()

        return self.find_element_base(Locators.locator_button_show_order).is_enabled()
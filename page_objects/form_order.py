from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

class UserInfoConstants:
    data_1 = {
        'first_name': 'Петр',
        'second_name': 'Петров',
        'address': 'Москва',
        'phone_number': '+79161234567',
        'order_comment': 'Тестовый комментарий 1'
    }
    data_2 = {
        'first_name': 'Иван',
        'second_name': 'Иванов',
        'address': 'Волгоград',
        'phone_number': '+79161112233',
        'order_comment': 'Тестовый комментарий 2'
    }


class FormOrder:
    #form user
    locator_input_first_name_form_order = (By.XPATH, '//input[@placeholder="* Имя"]')
    locator_input_second_name_form_order = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    locator_input_address_form_order = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    locator_input_metro_station_form_order = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    locator_input_choose_metro_station_form_order = (By.XPATH, '//div[@class="select-search__select"]/child::*/li[@data-value="2"]/child::button/child::div[@class="Order_Text__2broi"]')
    locator_input_phone_number_form_order = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    locator_button_next_form_order = (By.XPATH, '//button[contains(text(), "Далее")]')

    # form order
    locator_select_date_order = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    locator_option_date_order = (By.XPATH, '//div[@aria-label="Choose понедельник, 23-е декабря 2024 г."]')
    locator_select_period_order = (By.XPATH, '//div[@aria-haspopup="listbox"]')
    locator_option_period_order = (By.XPATH, '//div[contains(@class, "Dropdown-option") and text() = "сутки"]')
    locator_color_order = (By.XPATH, '//label[contains(@for, "black") and text() = "чёрный жемчуг"]')
    locator_input_comment = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    locator_button_make_order = (By.XPATH, '//button[contains(@class, "Button_Middle__1CSJM") and text() = "Заказать"]')

    # popup yes
    locator_popup_yes = (By.XPATH, '//div[@class="Order_Modal__YZ-d3"]')
    locator_button_yes = (By.XPATH, '//button[contains(text(), "Да")]')


    def __init__(self, driver):
        self.driver = driver

    @allure.step('Заполнение формы юзера')
    def complete_user_form(self, data):
        self.driver.find_element(*self.locator_input_first_name_form_order).send_keys(data['first_name'])
        self.driver.find_element(*self.locator_input_second_name_form_order).send_keys(data['second_name'])
        self.driver.find_element(*self.locator_input_address_form_order).send_keys(data['address'])
        self.driver.find_element(*self.locator_input_metro_station_form_order).click()
        self.driver.find_element(*self.locator_input_choose_metro_station_form_order).click()
        self.driver.find_element(*self.locator_input_phone_number_form_order).send_keys(data['phone_number'])
        self.driver.find_element(*self.locator_button_next_form_order).click()

    @allure.step('Заполнение формы заказа')
    def complete_order_form(self, data):
        self.driver.find_element(*self.locator_select_date_order).click()
        self.driver.find_element(*self.locator_option_date_order).click()
        self.driver.find_element(*self.locator_select_period_order).click()
        self.driver.find_element(*self.locator_option_period_order).click()
        self.driver.find_element(*self.locator_color_order).click()
        self.driver.find_element(*self.locator_input_comment).send_keys(data['order_comment'])
        self.driver.find_element(*self.locator_button_make_order).click()

    @allure.step('Открытие формы подтверждения заказа')
    def confirm_order(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.locator_popup_yes))
        self.driver.find_element(*self.locator_button_yes).click()


    def make_order(self, data):
        self.complete_user_form(data)
        self.complete_order_form(data)
        self.confirm_order()
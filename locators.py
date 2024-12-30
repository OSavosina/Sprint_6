from selenium.webdriver.common.by import By


class Locators:
    # accordion
    locator_accordion_heading = "//div[@id='{:s}']/parent::*"
    locator_accordion_panel = "//div[@id='{:s}']/p"
    
    # form user
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
    locator_button_show_order = (By.XPATH, '//button[contains(@class, "Button_Button__ra12g Button_Middle__1CSJM") and text() = "Посмотреть статус"]')

    # popup yes
    locator_popup_yes = (By.XPATH, '//div[@class="Order_Modal__YZ-d3"]')
    locator_button_yes = (By.XPATH, '//button[contains(text(), "Да")]')

    # main_page
    locator_button_get_cookies = (By.XPATH, '//button[@id="rcc-confirm-button"]')
    locator_popup_cookies = (By.XPATH, '//div[@class="App_CookieConsent__1yUIN"]')
    locator_top_button = (By.XPATH, '//button[@class="Button_Button__ra12g"]')
    locator_bottom_button = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    locator_logo_scooter = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')
    locator_logo_yandex = (By.XPATH, '//a[@href="//yandex.ru"]')


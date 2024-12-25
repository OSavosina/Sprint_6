from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

class Constants:
    ACCORDION_HEADING_COUNT = 8
    ACCORDION_HEADING_LOCATOR = "accordion__heading"
    ACCORDION_PANELS_LOCATOR = "accordion__panel"
    ACCORDION_PANELS_TEXTS = [
        'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
        'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
        'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
        'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
        'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
        'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
        'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
        'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
    ]


class AccordionQuestions:
    locators_dict_accordion_heading = {}
    locators_dict_accordion_panels = {}

    def make_locators_accordion(self):
        for item_id in range(Constants.ACCORDION_HEADING_COUNT):
            heading = (By.XPATH, f"//div[@id='{Constants.ACCORDION_HEADING_LOCATOR}-{item_id}']/parent::*")
            self.locators_dict_accordion_heading[f"ACCORDION_HEADING_{item_id}"] = heading

            panel = (By.XPATH, f"//div[@id='{Constants.ACCORDION_PANELS_LOCATOR}-{item_id}']/p")
            self.locators_dict_accordion_panels[f"ACCORDION_PANEL_{item_id}"] = panel


    def __init__(self, driver):
        self.make_locators_accordion()
        self.driver = driver

    @allure.step('Открытие ответа на вопрос из списка')
    def check_accordion_panel_is_enabled(self, item_id, expected_value):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((self.locators_dict_accordion_heading[f"ACCORDION_HEADING_{item_id}"])))
        self.driver.find_element(*self.locators_dict_accordion_heading[f"ACCORDION_HEADING_{item_id}"]).click()

        actually_value = self.driver.find_element(*self.locators_dict_accordion_panels[f"ACCORDION_PANEL_{item_id}"]).text
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'


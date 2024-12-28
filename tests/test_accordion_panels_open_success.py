import pytest
from page_objects.main_page import MainPage
from data import AccordionConstants
from conftest import driver
import allure


class TestAccordionPanelOpenSuccess:
    @allure.title('Открытие панелей с вопросами')
    @pytest.mark.parametrize('item', list(range(AccordionConstants.ACCORDION_HEADING_COUNT)))
    def test_accordion_panel_open_success(self, driver, item):
        accordion_questions = MainPage(driver)
        expected_value = AccordionConstants.ACCORDION_PANELS_TEXTS[item]
        actually_value = accordion_questions.check_accordion_panel_is_enabled(item, AccordionConstants.ACCORDION_PANELS_TEXTS[item])
        assert actually_value == expected_value, f'Ожидалось значение: "{expected_value}", получено "{actually_value}"'



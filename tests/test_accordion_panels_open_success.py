import pytest
from conftest import driver
from page_objects.accordion_questions import AccordionQuestions, Constants

accordion_heading = list(range(Constants.ACCORDION_HEADING_COUNT)) # Количество панелей
panel_texts = Constants.ACCORDION_PANELS_TEXTS # Список с текстами выпадающих панелей

class TestAccordionPanelOpenSuccess:
    @pytest.mark.parametrize('item', accordion_heading)
    def test_accordion_panel_open_success(self, driver, item):
            accordion_questions = AccordionQuestions(driver)
            accordion_questions.check_accordion_panel_is_enabled(item, panel_texts[item])


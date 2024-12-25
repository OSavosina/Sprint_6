import pytest
from conftest import driver
from page_objects.form_order import FormOrder
from page_objects.form_order import UserInfoConstants
from page_objects.main_page import MainPage


class TestMakeOrderByButtonSuccess:
     button_top = MainPage.locator_top_button
     button_bottom = MainPage.locator_bottom_button

     @pytest.mark.parametrize('order_data,button', [(UserInfoConstants.data_1, button_top), (UserInfoConstants.data_2, button_bottom)])
     def test_make_order_by_button_success(self, driver, order_data, button):
          form_order = FormOrder(driver)
          main_page = MainPage(driver)

          main_page.get_cookies()
          main_page.click_button_order(button)

          form_order.make_order(order_data)

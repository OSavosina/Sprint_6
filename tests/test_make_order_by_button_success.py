import allure
import pytest
from conftest import driver
from page_objects.order_page import OrderPage
from data import UserInfoConstants
from page_objects.main_page import MainPage
from locators import Locators


class TestMakeOrderByButtonSuccess:
     @allure.title('Оформление заказа')
     @pytest.mark.parametrize('order_data,button', [(UserInfoConstants.data_1, Locators.locator_top_button), (UserInfoConstants.data_2, Locators.locator_bottom_button)])
     def test_make_order_by_button_success(self, driver, order_data, button):
          form_order = OrderPage(driver)
          main_page = MainPage(driver)

          main_page.accept_cookies()
          main_page.click_button_order(button)

          order_made_success = form_order.make_order(order_data)
          assert order_made_success == True
          

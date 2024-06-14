import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:
    order_button_actions = {
        'Order button on header': OrderPage.make_order,
        'Order button with scroll': OrderPage.scroll_make_order
    }

    @pytest.mark.parametrize("order_button", list(order_button_actions.keys()))
    @allure.title("Тест проверяет создание заказа по кнопке в хедере и по кнопке ниже по скроллу")
    def test_make_order(self, driver, order_button):
        main_page = MainPage(driver)
        main_page.click_on_cookies()
        order_page = OrderPage(driver)
        self.order_button_actions[order_button](order_page)
        assert order_page.check_order_success_text()

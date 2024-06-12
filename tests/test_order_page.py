import allure
import pytest

from data import ORDER_SUCCESS_TEXT, ORDER_SUCCESS_TEXT_LOCATOR
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage


class TestOrderPage:
    @pytest.mark.parametrize(
        "order_button",
        [
            OrderPageLocators.ORDER_BUTTON,
            OrderPageLocators.ORDER_BUTTON_SCROLL
        ],
        ids=[
            'Order button on header',
            'Order button with scroll'
        ]
    )
    @allure.title("Тест проверяет создание заказа по кнопке в хедере и по кнопке ниже по скроллу")
    def test_make_order(self, driver, order_button):
        order_page = OrderPage(driver)
        order_actions = {
            OrderPageLocators.ORDER_BUTTON: order_page.make_order,
            OrderPageLocators.ORDER_BUTTON_SCROLL: order_page.scroll_make_order
        }
        order_actions[order_button]()
        assert ORDER_SUCCESS_TEXT in order_page.get_text_from_element(ORDER_SUCCESS_TEXT_LOCATOR)

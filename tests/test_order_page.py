import pytest

from data import ORDER_SUCCESS_TEXT
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
    def test_make_order(self, driver, order_button):
        order_page = OrderPage(driver)
        if order_button == OrderPageLocators.ORDER_BUTTON_SCROLL:
            order_page.scroll_make_order()
        else:
            order_page.make_order()

        assert ORDER_SUCCESS_TEXT in order_page.get_text_from_element(OrderPageLocators.ORDER_PLACED_TEXT)

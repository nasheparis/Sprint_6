import allure

from data import TEST_COMMENT
from helpers import generate_order_info
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Создание заказа по кнопке "Заказать" в хедере')
    def make_order(self):
        self.click_to_element(BasePageLocators.COOKIE_BUTTON)
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
        self.add_text_to_element(OrderPageLocators.FIRST_NAME_FIELD, generate_order_info()['first_name'])
        self.add_text_to_element(OrderPageLocators.LAST_NAME_FIELD, generate_order_info()['last_name'])
        self.add_text_to_element(OrderPageLocators.ADDRESS_FIELD, generate_order_info()['address'])
        self.click_to_element(OrderPageLocators.STATION_CHOICE)
        self.click_to_element(OrderPageLocators.FIRST_STATION)
        self.add_text_to_element(OrderPageLocators.PHONE_NUMBER_FIELD, generate_order_info()['phone_number'])
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)
        self.click_to_element(OrderPageLocators.TIME_FIELD)
        self.click_to_element(OrderPageLocators.DATEPICKER)
        self.click_to_element(OrderPageLocators.RENT_FIELD)
        self.click_to_element(OrderPageLocators.RENT_TERM_PICKER)
        self.click_to_element(OrderPageLocators.COLOUR_PICKER)
        self.add_text_to_element(OrderPageLocators.COMMENT_FIELD, TEST_COMMENT)
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_FORM)
        self.click_to_element(OrderPageLocators.YES_BUTTON)
        text = self.get_text_from_element(OrderPageLocators.ORDER_PLACED_TEXT)
        return text

    @allure.step('Создание заказа по кнопке "Заказать" ниже по скроллу')
    def scroll_make_order(self):
        self.click_to_element(BasePageLocators.COOKIE_BUTTON)
        element = self.find_element_with_wait(OrderPageLocators.ORDER_BUTTON_SCROLL)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_SCROLL)
        self.add_text_to_element(OrderPageLocators.FIRST_NAME_FIELD, generate_order_info()['first_name'])
        self.add_text_to_element(OrderPageLocators.LAST_NAME_FIELD, generate_order_info()['last_name'])
        self.add_text_to_element(OrderPageLocators.ADDRESS_FIELD, generate_order_info()['address'])
        self.click_to_element(OrderPageLocators.STATION_CHOICE)
        self.click_to_element(OrderPageLocators.FIRST_STATION)
        self.add_text_to_element(OrderPageLocators.PHONE_NUMBER_FIELD, generate_order_info()['phone_number'])
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)
        self.click_to_element(OrderPageLocators.TIME_FIELD)
        self.click_to_element(OrderPageLocators.DATEPICKER)
        self.click_to_element(OrderPageLocators.RENT_FIELD)
        self.click_to_element(OrderPageLocators.RENT_TERM_PICKER)
        self.click_to_element(OrderPageLocators.COLOUR_PICKER)
        self.add_text_to_element(OrderPageLocators.COMMENT_FIELD, TEST_COMMENT)
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_FORM)
        self.click_to_element(OrderPageLocators.YES_BUTTON)
        text = self.get_text_from_element(OrderPageLocators.ORDER_PLACED_TEXT)
        return text
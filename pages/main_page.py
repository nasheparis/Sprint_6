import allure

from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Получение текста ответа")
    def get_answer_text(self, num):
        self.click_to_element(BasePageLocators.COOKIE_BUTTON)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER, num)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    def click_on_logo(self):
        self.click_to_element(BasePageLocators.SCOOTER_LOGO)
        link = self.driver.current_url
        return link




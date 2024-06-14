import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Получение текста ответа")
    def get_answer_text(self, num):
        self.click_on_cookies()
        self.scroll_to_end()
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER, num)
        self.click_to_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step("Проверка перехода на главную страницу по тапу на слово 'Самокат' в хедере")
    def click_on_logo(self):
        self.click_to_element(MainPageLocators.SCOOTER_LOGO)
        link = self.get_current_url()
        return link

    @allure.step("Клик на куки")
    def click_on_cookies(self):
        self.click_to_element(MainPageLocators.COOKIE_BUTTON)

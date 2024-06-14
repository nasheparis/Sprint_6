import allure

from locators.external_page_locators import ExternalPageLocators
from pages.base_page import BasePage


class ExternalPage(BasePage):
    @allure.step("Переход по внешней ссылке")
    def follow_external_link(self):
        self.click_to_element(ExternalPageLocators.YANDEX_BUTTON)
        new_tab = self.get_window_tabs()
        self.switch_to_window(new_tab)
        self.find_element_with_wait(ExternalPageLocators.INSTALL_BUTTON)
        text = self.get_text_from_element(ExternalPageLocators.INSTALL_BUTTON)
        return text






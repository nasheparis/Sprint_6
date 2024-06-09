import time

import allure

from locators.base_page_locators import BasePageLocators
from locators.external_page_locators import ExternalPageLocators
from pages.base_page import BasePage


class ExternalPage(BasePage):
    @allure.step("Переход по внешней ссылке")
    def follow_external_link(self):
        self.click_to_element(BasePageLocators.YANDEX_BUTTON)
        new_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(new_tab)
        self.find_element_with_wait(ExternalPageLocators.INSTALL_BUTTON)
        text = self.get_text_from_element(ExternalPageLocators.INSTALL_BUTTON)
        return text






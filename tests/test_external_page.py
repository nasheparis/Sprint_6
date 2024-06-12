import allure

from data import YANDEX_INSTALL_BUTTON, YANDEX_INSTALL_BUTTON_TEXT
from pages.external_page import ExternalPage


class TestExternalPage:
    @allure.title("Проверка перехода по внешней ссылке по тапу на лого")
    def test_click_external_link(self, driver):
        external_page = ExternalPage(driver)
        external_page.follow_external_link()
        assert external_page.get_text_from_element(YANDEX_INSTALL_BUTTON) == YANDEX_INSTALL_BUTTON_TEXT



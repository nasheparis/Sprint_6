from locators.external_page_locators import ExternalPageLocators
from pages.external_page import ExternalPage


class TestExternalPage:
    def test_click_external_link(self, driver):
        external_page = ExternalPage(driver)
        external_page.follow_external_link()
        assert external_page.get_text_from_element(ExternalPageLocators.INSTALL_BUTTON) == 'Установить'



from selenium.webdriver.common.by import By


class ExternalPageLocators:
    YANDEX_BUTTON = By.XPATH, '//img[contains(@src, "ya.svg")]'
    INSTALL_BUTTON = By.XPATH, '//a[contains(@title, "Установить")]'

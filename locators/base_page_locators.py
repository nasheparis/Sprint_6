from selenium.webdriver.common.by import By


class BasePageLocators:
    COOKIE_BUTTON = By.XPATH, '//button[contains(text(), "все привыкли")]'
    YANDEX_BUTTON = By.XPATH, '//img[contains(@src, "ya.svg")]'
    SCOOTER_LOGO = By.CSS_SELECTOR, '[class*="Header_LogoScooter"]'




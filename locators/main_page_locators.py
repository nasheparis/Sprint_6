from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION = By.ID, 'accordion__heading-{}'
    ANSWER = By.ID, 'accordion__panel-{}'
    COOKIE_BUTTON = By.XPATH, '//button[contains(text(), "все привыкли")]'
    SCOOTER_LOGO = By.CSS_SELECTOR, '[class*="Header_LogoScooter"]'



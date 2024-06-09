from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_BUTTON = By.XPATH, '//button[contains(text(), "Заказать")]'
    FIRST_NAME_FIELD = By.XPATH, '//input[contains(@placeholder, "Имя")]'
    LAST_NAME_FIELD = By.XPATH, '//input[contains(@placeholder, "Фамилия")]'
    ADDRESS_FIELD = By.XPATH, '//input[contains(@placeholder, "Адрес: куда привезти заказ")]'
    STATION_CHOICE = By.XPATH, '//input[contains(@placeholder, "Станция метро")]'
    FIRST_STATION = By.XPATH, '//*[contains(@data-value, "1")]'
    PHONE_NUMBER_FIELD = By.XPATH, '//input[contains(@placeholder, "Телефон: на него позвонит курьер")]'
    NEXT_BUTTON = By.XPATH, '//button[contains(text(), "Далее")]'
    TIME_FIELD = By.XPATH, '//input[contains(@placeholder, "Когда привезти самокат")]'
    DATEPICKER = By.XPATH, '//div[contains(@class, "react-datepicker__day react-datepicker__day--028")]'
    RENT_FIELD = By.XPATH, '//div[contains(text(), "Срок аренды")]'
    RENT_TERM_PICKER = By.XPATH, '//div[contains(text(), "сутки")]'
    COLOUR_PICKER = By.XPATH, '//input[@id="black"]'
    COMMENT_FIELD = By.XPATH, '//input[contains(@placeholder, "Комментарий для курьера")]'
    ORDER_BUTTON_FORM = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]'
    YES_BUTTON = By.XPATH, '//button[contains(text(), "Да")]'
    ORDER_PLACED_TEXT = By.XPATH, '//div[contains(text(), "Заказ оформлен")]'
    STATUS_BUTTON = By.XPATH, '//button[contains(text(), "Посмотреть статус")]'
    CANCEL_ORDER = By.XPATH, '//button[contains(text(), "Отменить заказ")]'
    ORDER_BUTTON_SCROLL = By.XPATH, '//div[contains(@class, "Home_FinishButton")]'

from locators.external_page_locators import ExternalPageLocators
from locators.order_page_locators import OrderPageLocators

WEBSITE = 'https://qa-scooter.praktikum-services.ru/'
TEST_COMMENT = 'test'
ORDER_SUCCESS_TEXT_LOCATOR = OrderPageLocators.ORDER_PLACED_TEXT
ORDER_SUCCESS_TEXT = 'Заказ оформлен'
YANDEX_INSTALL_BUTTON = ExternalPageLocators.INSTALL_BUTTON
YANDEX_INSTALL_BUTTON_TEXT = 'Установить'


class AnswerTexts:
    ANSWER_PRICE = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    ANSWER_QUANTITY_PER_ORDER = ('Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
                                 'можете просто сделать несколько заказов — один за другим.')
    ANSWER_RENT_PERIOD = ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт '
                          'времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли '
                          'самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')
    ANSWER_ORDER_TERM = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    ANSWER_PROLONG_OR_RETURN = ('Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по '
                                'красивому номеру 1010.')
    ANSWER_CHARGE = ('Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете '
                     'кататься без передышек и во сне. Зарядка не понадобится.')
    ANSWER_CANCEL = ('Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же '
                     'свои.')
    ANSWER_LOCATION = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

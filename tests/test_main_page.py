import pytest

from data import AnswerTexts, WEBSITE
from pages.main_page import MainPage


class TestMainPage:

    @pytest.mark.parametrize(
        'num, result',
        [
            (0, AnswerTexts.ANSWER_PRICE),
            (1, AnswerTexts.ANSWER_QUANTITY_PER_ORDER),
            (2, AnswerTexts.ANSWER_RENT_PERIOD),
            (3, AnswerTexts.ANSWER_ORDER_TERM),
            (4, AnswerTexts.ANSWER_PROLONG_OR_RETURN),
            (5, AnswerTexts.ANSWER_CHARGE),
            (6, AnswerTexts.ANSWER_CANCEL),
            (7, AnswerTexts.ANSWER_LOCATION),
        ],
        ids=[
            'answer 1: price',
            'answer 2: quantity',
            'answer 3: rent period',
            'answer 4: order term',
            'answer 5: prolongation or return',
            'answer 6: charging',
            'answer 7: cancellation',
            'answer 8: location'
        ]
    )
    def test_get_faq(self, driver, num, result):
        main_page = MainPage(driver)
        assert main_page.get_answer_text(num) == result

    def test_click_on_logo(self, driver):
        main_page = MainPage(driver)
        expected_url = WEBSITE
        actual_url = main_page.click_on_logo()
        assert actual_url == expected_url

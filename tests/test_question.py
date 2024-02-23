import allure
from pages.question_page import QuestionPage
from locators.question_locators import QuestionPageLocator
import pytest
from data import TestData


class TestQuestionPage:

    @pytest.mark.parametrize('num, answer_text', (
            (
                    (0, TestData.answer_texts[0]),
                    (1, TestData.answer_texts[1]),
                    (2, TestData.answer_texts[2]),
                    (3, TestData.answer_texts[3]),
                    (4, TestData.answer_texts[4]),
                    (5, TestData.answer_texts[5]),
                    (6, TestData.answer_texts[6]),
                    (7, TestData.answer_texts[7])
            )
                             ))
    @allure.title ('Проверка текста ответов в "Вопросы о важном"')
    @allure.description ('На главной странице скроллим до блока "Вопросы о важном". \
                         Кликаем на вопрос, проверяем отображение и текст ответа')
    def test_answers(self, driver, num, answer_text):
        question_page = QuestionPage(driver)
        question_page.scroll_to_element(QuestionPageLocator.LAST_QUESTION_LOCATOR)
        result = question_page.click_on_element_and_get_text(
            QuestionPageLocator.QUESTION_LOCATOR,
            QuestionPageLocator.ANSWER_LOCATOR,
            num
        )
        assert question_page.check_answer_text(result, answer_text), \
            f'Ожидаемый результат: "{answer_text}", фактический результат: "{result}"'

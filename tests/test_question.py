import allure
from pages.question_page import QuestionPage
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
        question_page.accept_cookie()
        question_page.scroll_to_last_question()
        result = question_page.click_on_element_and_get_text(num)
        assert question_page.check_answer_text(result, answer_text), \
            f'Ожидаемый результат: "{answer_text}", фактический результат: "{result}"'

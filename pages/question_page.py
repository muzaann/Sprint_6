from pages.base_page import BasePage
from locators.question_locators import QuestionPageLocator
import allure

class QuestionPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step ('Клик по кнопке "да все привыкли" в блоке принятия Куки')
    def accept_cookie(self):
        self.click_on_element(QuestionPageLocator.ACСEPT_COOKIE)
    @allure.step ('Скролл до последненего вопроса в блоке "Вопросы о важном"')
    def scroll_to_last_question(self):
        self.scroll_to_element(QuestionPageLocator.LAST_QUESTION_LOCATOR)
    @allure.step ('Клик по вопросу, получение текста ответа на вопрос')
    def click_on_element_and_get_text(self, num):
        method_q, locator_q = QuestionPageLocator.QUESTION_LOCATOR
        locator_q = locator_q.format(num)
        method_a, locator_a = QuestionPageLocator.ANSWER_LOCATOR
        locator_a = locator_a.format(num)
        self.scroll_and_click_with_wait((method_q, locator_q))
        return self.get_text_by_element((method_a, locator_a))
    @allure.step ('Сравнение полученного ответа с ожидаемым')
    def check_answer_text(self, result, answer_text):
        return result == answer_text



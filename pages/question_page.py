from pages.base_page import BasePage


class QuestionPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)


    def click_on_element_and_get_text(self, locator_question, locator_answer, num):

        method_q, locator_q = locator_question
        locator_q = locator_q.format(num)
        method_a, locator_a = locator_answer
        locator_a = locator_a.format(num)
        self.click_on_element((method_q, locator_q))
        return self.get_text_by_element((method_a, locator_a))
    def check_answer_text(self, result, answer_text):
        return result == answer_text



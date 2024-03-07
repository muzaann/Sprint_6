from selenium.webdriver.common.by import By


class QuestionPageLocator:
    ACСEPT_COOKIE = By.ID, "rcc-confirm-button"
    LAST_QUESTION_LOCATOR = By.ID, "accordion__heading-7"
    QUESTION_LOCATOR = By.ID, "accordion__heading-{}"
    ANSWER_LOCATOR = By.ID, "accordion__panel-{}"

import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocator



class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step ('Клик по лого "Самокат" из окна оформления заказа')
    def check_click_logo_scooter(self):
        self.click_on_element(MainPageLocator.ORDER_BUTTON_HEADER)
        self.click_on_element(MainPageLocator.LOGO_SCOOTER_LOCATOR)
    @allure.step ('Проверка текста на главной странице для подтверждения перехода на главную страницу')
    def get_text_on_main_page(self):
        return self.get_text_by_element(MainPageLocator.TEXT_SCOOTER)

    @allure.step ('Клик по лого "Яндекс", переход к открывшемуся окну, закрытие всплывающего окна "Яндекс.Браузер", если оно появилось')
    def check_click_logo_dzen(self):
        self.click_on_element(MainPageLocator.DZEN_LOGO_BUTTON_LOCATOR)
        self.switch_to_window(1)
        if self.wait_and_find_element(MainPageLocator.WINDOW_TEXT):
            self.click_on_element(MainPageLocator.ClOSE_WINDOWS_BUTTON)
        else:
            pass

    @allure.step('Проверка наличия на странице шапки сайта "Дзен"')
    def check_search_field(self):
        return self.wait_and_find_element(MainPageLocator.SEARCH_DZEN_BUTTON).get_attribute('aria-label')








from pages.base_page import BasePage
import time

class MainPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def check_click_logo_scooter(self, locator_order_button, locator_logo_scooter):
        self.click_on_element(locator_order_button)
        self.click_on_element(locator_logo_scooter)

    def check_click_logo_dzen(self, locator_logo_dzen, number, pop_up_window_locator, close_button_logo):
        self.click_on_element(locator_logo_dzen)

        self.switch_to_window(number)

        if self.wait_and_find_element(pop_up_window_locator):
            self.click_on_element(close_button_logo)
        else:
            print('Не появилось  всплывающее окно Яндекс.Браузер')






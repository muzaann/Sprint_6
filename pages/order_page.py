import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocator


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик на кнопку "Заказать"')
    def click_any_order_button(self, is_up_button):
        if is_up_button:
            self.click_on_element(OrderPageLocator.ORDER_BUTTON_HEADER)
        else:
            self.scroll_and_click_with_wait(OrderPageLocator.ORDER_BUTTON)


    @allure.step('Заполнение полей формы "Для кого самокат"')
    def set_customer_info(self, is_up_button, text_name, text_surname, text_adress, metro_station, text_phone):
        self.click_any_order_button(is_up_button)
        self.set_text_to_element(OrderPageLocator.NAME_FIELD, text_name)
        self.set_text_to_element(OrderPageLocator.SURNAME_FIELD, text_surname)
        self.set_text_to_element(OrderPageLocator.ADRESS_FIELD, text_adress)
        self.click_on_element(OrderPageLocator.METRO_STATION)
        method_m, locator_m = OrderPageLocator.ANY_STATION
        locator_m = locator_m.format(metro_station)
        self.scroll_and_click_with_wait((method_m, locator_m))
        self.set_text_to_element(OrderPageLocator.PHONE_NUMBER, text_phone)
        self.scroll_and_click_with_wait(OrderPageLocator.ONWARDS_BUTTON)

    @allure.step('Заполнение полей формы "Про аренду"')
    def set_rent_info(self, delivery_date, time_rent, color, text_comment):
        self.wait_and_find_element(OrderPageLocator.RENT_BLOCK)
        self.click_on_element(OrderPageLocator.WHEN_DELIVERY_FIELD)
        method_d, locator_d = OrderPageLocator.DELIVERY_DATE
        locator_d = locator_d.format(delivery_date)
        self.click_on_element((method_d, locator_d))
        self.click_on_element(OrderPageLocator.TIME_RENT_FIELD)
        method_t, locator_t = OrderPageLocator.TIME_RENT
        locator_t = locator_t.format(time_rent)
        self.click_on_element((method_t, locator_t))
        self.wait_and_find_element(OrderPageLocator.SCOOTER_COLOR)
        method_c, locator_c = OrderPageLocator.CHOOSE_COLOR
        locator_c = locator_c.format(color)
        self.click_on_element((method_c, locator_c))
        self.set_text_to_element(OrderPageLocator.COMMENT, text_comment)
        self.click_on_element(OrderPageLocator.FINAL_ORDER_BUTTON)
        self.wait_and_find_element(OrderPageLocator.ORDER_BLOCK)
        self.click_on_element(OrderPageLocator.YES_BUTTON)

    @allure.step('Получение текста кнопки вспылающего окна об успешном создании заказа')
    def get_button_text(self):
        return self.get_text_by_element(OrderPageLocator.LOOK_STATUS_BUTTON)
    @allure.step('Сравнение полученного текста с ожидаемым')
    def check_button_text(self, result, button_text):
        return result == button_text












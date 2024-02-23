from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def scroll_and_click(self, locator):
        self.scroll_to_element(locator)
        self.click_on_element(locator)

    def set_customer_info(self, locator_button_order, locator_name, text_name, locator_surname,
                          text_surname, locator_adress, text_adress, locator_metro,
                          locator_metro_station, locator_phone, text_phone, locator_onwards):
        self.scroll_and_click(locator_button_order)
        self.set_text_to_element(locator_name, text_name)
        self.set_text_to_element(locator_surname, text_surname)
        self.set_text_to_element(locator_adress, text_adress)
        self.click_on_element(locator_metro)
        self.scroll_and_click(locator_metro_station)
        self.set_text_to_element(locator_phone, text_phone)
        self.scroll_and_click(locator_onwards)

    def set_rent_info(self, locator_rent_block, locator_when_delivery, when_text, locator_time_rent,
                      locator_value_time_rent, locator_color, locator_choose_color,  locator_comment,
                      text_comment, locator_order_button, locator_order_block, locator_yes_button):
        self.wait_and_find_element(locator_rent_block)
        self.click_on_element(locator_when_delivery)
        self.click_on_element(when_text)
        self.click_on_element(locator_time_rent)

        self.click_on_element(locator_value_time_rent)
        self.wait_and_find_element(locator_color)
        self.click_on_element(locator_choose_color)
        self.set_text_to_element(locator_comment, text_comment)
        self.click_on_element(locator_order_button)
        self.wait_and_find_element(locator_order_block)
        self.click_on_element(locator_yes_button)

    def check_button_text(self, locator_status_button, button_text):
        result = self.get_text_by_element(locator_status_button)
        return result == button_text












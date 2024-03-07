import allure
from pages.order_page import OrderPage
import pytest
from data import TestData


class TestOrderPage:

    @pytest.mark.parametrize('is_up_button, name, surname, adress, metro, phone, date, days, color, comment', (
            (
                    (True, TestData.names[0], TestData.surnames[0], TestData.adress[0],
                     TestData.metro_station[0], TestData.phone[0], TestData.delivery_date[0],
                     TestData.time_rent[0], TestData.color_scooter[0], TestData.comment[0]),
                    (False, TestData.names[1], TestData.surnames[1], TestData.adress[1],
                     TestData.metro_station[1], TestData.phone[1], TestData.delivery_date[1],
                     TestData.time_rent[1], TestData.color_scooter[1], TestData.comment[1])
            )
    ))
    @allure.title('Позитивная проверка оформления заказа самоката с двумя наборами тестовых данных')
    @allure.description('Кликаем на кнопку "Заказать", заполняем формы "Для кого самокат" и "Про аренду",\
                        проверяем появление всплывающего окна о создании заказа с кнопкой "Посмотреть статус"')
    def test_order_block_customer(self, driver, is_up_button, name, surname, adress, metro, phone, date, days, color, comment):
        order_page = OrderPage(driver)
        order_page.set_customer_info(is_up_button, name, surname, adress, metro, phone)
        order_page.set_rent_info(date, days, color, comment)
        result = order_page.get_button_text()
        assert order_page.check_button_text(result,'Посмотреть статус'), \
            f'Ожидаемый результат: "Посмотреть статус", фактический результат: "{result}"'

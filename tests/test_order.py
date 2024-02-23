import allure
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocator
import pytest
from data import TestData


class TestQuestionPage:

    @pytest.mark.parametrize('button, name, surname, adress, metro, phone, date, days, color, comment', (
            (
                    (OrderPageLocator.ORDER_BUTTON_HEADER, TestData.names[0],
                     TestData.surnames[0], TestData.adress[0], OrderPageLocator.TEATROLNAYA_STATION,
                     TestData.phone[0], OrderPageLocator.DELIVERY_DATE_28_FEB, OrderPageLocator.TIME_RENT_4,
                     OrderPageLocator.BLACK_SCOOTER, TestData.comment[0]),
                    (OrderPageLocator.ORDER_BUTTON, TestData.names[1],
                     TestData.surnames[1], TestData.adress[1],
                     OrderPageLocator.KRASNIE_VOROTA_STATION, TestData.phone[1], OrderPageLocator.DELIVERY_DATE_2_MARCH,
                     OrderPageLocator.TIME_RENT_1, OrderPageLocator.GREY_SCOOTER, TestData.comment[1])
            )
    ))
    @allure.title('Позитивная проверка оформления заказа самоката с двумя наборами тестовых данных')
    @allure.description('Кликаем на кнопку "Заказать", заполняем формы "Для кого самокат" и "Про аренду",\
                        проверяем появление всплывающего окна с сообщением об успешном создании заказа')
    def test_order_block_customer(self, driver, button, name, surname, adress, metro, phone, date, days, color, comment):
        order_page = OrderPage(driver)
        order_page.set_customer_info(
            button, OrderPageLocator.NAME_FIELD, name, OrderPageLocator.SURNAME_FIELD, surname,
            OrderPageLocator.ADRESS_FIELD, adress, OrderPageLocator.METRO_STATION, metro,
            OrderPageLocator.PHONE_NUMBER, phone, OrderPageLocator.ONWARDS_BUTTON
        )

        order_page.set_rent_info(
            OrderPageLocator.RENT_BLOCK, OrderPageLocator.WHEN_DELIVERY_FIELD,
            date, OrderPageLocator.TIME_RENT_FIELD, days, OrderPageLocator.SCOOTER_COLOUR, color,
            OrderPageLocator.COMMENT, comment, OrderPageLocator.FINAL_ORDER_BUTTON,
            OrderPageLocator.ORDER_BLOCK, OrderPageLocator.YES_BUTTON
        )

        assert order_page.check_button_text(
            OrderPageLocator.LOOK_STATUS_BUTTON, 'Посмотреть статус'), \
            f'Ожидаемый результат: "Посмотреть статус", фактический результат: "{result}"'

import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocator


class TestTransitions:
    @allure.title('Проверка перехода на главную страницу при клике на лого "Самокат"')
    @allure.description('Кликаем на кнопку "Заказать", на странице заказа кликаем на лого "Самокат", \
                        проверяем переход на главную страницу приложения')
    def test_transition_logo_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.check_click_logo_scooter(
            MainPageLocator.ORDER_BUTTON_HEADER,
            MainPageLocator.LOGO_SCOOTER_LOCATOR
            )
        assert main_page.get_text_by_element(MainPageLocator.TEXT_SCOOTER) == \
        'Самокат\nна пару дней\nПривезём его прямо к вашей двери,\nа когда накатаетесь — заберём'

    @allure.title('Проверка перехода на главную страницу "Дзен" при клике на лого "Яндекс"')
    @allure.description('Кликаем на лого "Яндекс", проверяем что произошло открытие главной страницы \
                        Дзен в новом окне')
    def test_transition_logo_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.check_click_logo_dzen(
            MainPageLocator.DZEN_LOGO_BUTTON_LOCATOR,
            1,
            MainPageLocator.WINDOW_TEXT,
            MainPageLocator.ClOSE_WINDOWS_BUTTON
        )
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'

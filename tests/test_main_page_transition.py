import allure
from pages.main_page import MainPage



class TestTransitions:
    @allure.title('Проверка перехода на главную страницу при клике на лого "Самокат"')
    @allure.description('Кликаем на кнопку "Заказать", на странице заказа кликаем на лого "Самокат", \
                        проверяем переход на главную страницу приложения')
    def test_transition_logo_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.check_click_logo_scooter()
        assert main_page.get_text_on_main_page() == \
        'Самокат\nна пару дней\nПривезём его прямо к вашей двери,\nа когда накатаетесь — заберём'

    @allure.title('Проверка перехода на главную страницу "Дзен" при клике на лого "Яндекс"')
    @allure.description('Кликаем на лого "Яндекс", проверяем что произошло открытие главной страницы \
                        Дзен в новом окне, проверяем наличие шапки сайта Дзен и свреяем URL')
    def test_transition_logo_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.check_click_logo_dzen()
        assert main_page.check_search_field() == 'Шапка сайта' and 'dzen.ru' in driver.current_url

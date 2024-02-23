from selenium.webdriver.common.by import By


class MainPageLocator:
    ORDER_BUTTON_HEADER = By.XPATH, "//*[contains(@class, 'Button_Button') and text()='Заказать' and not(contains(@class, 'Button_Middle'))]"
    LOGO_SCOOTER_LOCATOR = By.XPATH, "//*[contains(@class, 'Header_LogoScooter')]"
    DZEN_LOGO_BUTTON_LOCATOR = By.XPATH, "//*[@href= '//yandex.ru']"
    TEXT_SCOOTER = By.XPATH, "//*[contains(@class, 'Home_Header')]"
    WINDOW_TEXT = By.XPATH, "//*[@title= 'Установить']"
    ClOSE_WINDOWS_BUTTON = By.TAG_NAME, "polygon"



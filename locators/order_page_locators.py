from selenium.webdriver.common.by import By


class OrderPageLocator:
    ORDER_BUTTON_HEADER = By.XPATH, "//*[contains(@class, 'Button_Button') and text()='Заказать' and not(contains(@class, 'Button_Middle'))]"
    ORDER_BUTTON = By.XPATH, "//*[contains(@class, 'Button_Middle') and text()='Заказать']"

    NAME_FIELD = By.XPATH, "//*[@placeholder='* Имя']"
    SURNAME_FIELD = By.XPATH, "//*[@placeholder='* Фамилия']"
    ADRESS_FIELD = By.XPATH, "//*[@placeholder='* Адрес: куда привезти заказ']"
    METRO_STATION = By.XPATH, "//*[@placeholder='* Станция метро']"
    ANY_STATION = By.XPATH, "//div[text()='{}']"
    PHONE_NUMBER = By.XPATH, "//*[@placeholder='* Телефон: на него позвонит курьер']"
    ONWARDS_BUTTON = By.XPATH, "//button[text()= 'Далее']"

    RENT_BLOCK = By.XPATH, "//div[text()= 'Про аренду']"
    WHEN_DELIVERY_FIELD = By.XPATH, "//*[@placeholder='* Когда привезти самокат']"
    DELIVERY_DATE = By.XPATH, "//*[@class='{}']"
    TIME_RENT_FIELD = By.XPATH, "//*[@class='Dropdown-control']"
    TIME_RENT = By.XPATH, "//div[text()='{}']"
    SCOOTER_COLOR = By.XPATH, "//div[text()='Цвет самоката']"
    CHOOSE_COLOR = By.XPATH, "//*[@for='{}']"
    COMMENT = By.XPATH, "//*[@placeholder='Комментарий для курьера']"
    FINAL_ORDER_BUTTON = By.XPATH, "//*[contains(@class, 'Button_Middle') and text()='Заказать']"
    ORDER_BLOCK = By.XPATH, "//*[contains(@class, 'Order_ModalHeader')]"
    YES_BUTTON = By.XPATH, "//*[contains(@class, 'Button_Middle') and text()='Да']"
    LOOK_STATUS_BUTTON = By.XPATH, "//*[contains(@class, 'Order_NextButton')]"

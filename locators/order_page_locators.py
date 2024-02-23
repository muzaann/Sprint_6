from selenium.webdriver.common.by import By


class OrderPageLocator:
    ORDER_BUTTON_HEADER = By.XPATH, "//*[contains(@class, 'Button_Button') and text()='Заказать' and not(contains(@class, 'Button_Middle'))]"
    ORDER_BUTTON = By.XPATH, "//*[contains(@class, 'Button_Middle') and text()='Заказать']"

    NAME_FIELD = By.XPATH, "//*[@placeholder='* Имя']"
    SURNAME_FIELD = By.XPATH, "//*[@placeholder='* Фамилия']"
    ADRESS_FIELD = By.XPATH, "//*[@placeholder='* Адрес: куда привезти заказ']"
    METRO_STATION = By.XPATH, "//*[@placeholder='* Станция метро']"
    TEATROLNAYA_STATION = By.XPATH, "//div[text()='Театральная']"
    KRASNIE_VOROTA_STATION = By.XPATH, "//div[text()='Красные Ворота']"
    PHONE_NUMBER = By.XPATH, "//*[@placeholder='* Телефон: на него позвонит курьер']"
    ONWARDS_BUTTON = By.XPATH, "//button[text()= 'Далее']"

    RENT_BLOCK = By.XPATH, "//div[text()= 'Про аренду']"
    WHEN_DELIVERY_FIELD = By.XPATH, "//*[@placeholder='* Когда привезти самокат']"
    DELIVERY_DATE_28_FEB = By.XPATH, "//*[@class='react-datepicker__day react-datepicker__day--028']"
    DELIVERY_DATE_2_MARCH = By.XPATH, "//*[@class='react-datepicker__day react-datepicker__day--002 react-datepicker__day--weekend react-datepicker__day--outside-month']"
    TIME_RENT_FIELD = By.XPATH, "//*[@class='Dropdown-control']"
    TIME_RENT_4 = By.XPATH, "//div[text()='четверо суток']"
    TIME_RENT_1 = By.XPATH, "//div[text()='сутки']"
    SCOOTER_COLOUR = By.XPATH, "//div[text()='Цвет самоката']"
    BLACK_SCOOTER = By.XPATH, "//*[@for='black']"
    GREY_SCOOTER = By.XPATH, "//*[@for='grey']"
    COMMENT = By.XPATH, "//*[@placeholder='Комментарий для курьера']"
    FINAL_ORDER_BUTTON = By.XPATH, "//*[contains(@class, 'Button_Middle') and text()='Заказать']"
    ORDER_BLOCK = By.XPATH, "//*[contains(@class, 'Order_ModalHeader')]"
    YES_BUTTON = By.XPATH, "//*[contains(@class, 'Button_Middle') and text()='Да']"
    LOOK_STATUS_BUTTON = By.XPATH, "//*[contains(@class, 'Button_Middle') and text()='Посмотреть статус']"
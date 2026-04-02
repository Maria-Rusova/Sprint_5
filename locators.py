from selenium.webdriver.common.by import By

class RegPage:
    NAME_INPUT = (By.XPATH, './/label[text()="Имя"]//parent::*/input')               # для поля "Имя" в форме регистрации
    EMAIL_INPUT = (By.XPATH, './/label[text()="Email"]//parent::*/input')            # для поля "Email" в форме регистрации
    PASSWORD_INPUT = (By.XPATH, './/input[@type="password"]')                        # для поля "password" в форме регистрации
    REGISTRATE_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]')         # для кнопки "Зарегистрироваться"
    LOGIN_TEXT_WITH_HREF = (By.CLASS_NAME, 'Auth_link__1fOlj')                       # для "Войти"
    INPUT_ERROR_TEXT = (By.XPATH, '//p[contains(text(), "Некорректный пароль")]')    # для Ошибки ввода в форме регистрации

class LoginPage:
    TITLE_TEXT = (By.XPATH, './/h2[text()="Вход"]')                                  # для текста Вход
    EMAIL_FIELD = (By.XPATH, './/label[text()="Email"]//parent::*/input')            # для поля Email
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/..//input")               # для поля password
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')                           # для кнопки Войти
    LOGIN_TEXT_WITH_HREF =(By.CLASS_NAME, 'Auth_link__1fOlj')                        # для Восстановить пароль

class MainPage:
    PROFILE_LINK_TEXT = (By.XPATH, './/p[text()="Личный Кабинет"]')                  # для перехода по ссылке "Личный кабинет"
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]')                 # для кнопки "Войти в аккаунт"
    ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')                  # Для "Оформить заказ"
    CONSTRUCTOR_LINK_TEXT = (By.XPATH, './/p[text()="Конструктор"]')                 # для перехода в "Конструктор"
    BUNS_TAB = (By.XPATH, './/span[text()="Булки"]/parent::*')                       # для Булки в Конструкторе
    SAUCES_TAB = (By.XPATH, './/span[text()="Соусы"]/parent::*')                     # для Соусы в Конструкторе
    FILLINGS_TAB = (By.XPATH, './/span[text()="Начинки"]/parent::*')                 # для Начинки в Конструкторе
    BUNS_SECTION_HEADER = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_SECTION_HEADER = (By.XPATH, "//h2[text()='Соусы']")
    FILLINGS_SECTION_HEADER = (By.XPATH, "//h2[text()='Начинки']")                 
    # ACTIVE_TAB_CLASS = 'tab_tab_type_current__2BEPc'                                # активная вкладка

class ProfilePage:
    INFO_TEXT = (By.XPATH, './/p[contains(text(),"персональные данные")]')           # инфо персональные данные
    HISTORY_LINK_TEXT = (By.XPATH, './/a[text()="История заказов"]')                 # для перехода в История заказов
    CONSTRUCTOR_LINK_TEXT = (By.XPATH, './/p[text()="Конструктор"]')                 # для перехода в Конструктор
    MAIN_LOGO = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')                     # для перехода на главную
    LOGOUT_BUTTON = (By.XPATH, './/button[text()="Выход"]')                          # для Выход
    H1_TITLE = (By.CSS_SELECTOR, "h1")

    
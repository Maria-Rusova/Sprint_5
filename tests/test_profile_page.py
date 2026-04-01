from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Urls
from locators import *

class TestProfilePage:

    def test_click_profile_link_open_profile_page(self, login: WebDriver) -> None:                                # переход по клику на ЛК
        driver = login
        driver.find_element(*MainPage.PROFILE_LINK_TEXT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePage.INFO_TEXT))
        assert driver.current_url == Urls.profile_page
        assert driver.find_element(*ProfilePage.INFO_TEXT).is_displayed()

    def test_click_constructor_link_show_constructor(self, login: WebDriver) -> None:                             # переход по клику на Конструктор
        driver = login
        driver.find_element(*MainPage.PROFILE_LINK_TEXT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePage.INFO_TEXT))
        driver.find_element(*ProfilePage.CONSTRUCTOR_LINK_TEXT).click()
        h1_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePage.H1_TITLE))
        assert h1_element.text == 'Соберите бургер'

    def test_click_main_logo_show_constructor(self, login: WebDriver) -> None:                                    # переход по клику на логотип Stellar Burgers.
        driver = login
        driver.find_element(*MainPage.PROFILE_LINK_TEXT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePage.INFO_TEXT))
        driver.find_element(*ProfilePage.MAIN_LOGO).click()
        h1_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePage.H1_TITLE))
        assert h1_element.text == 'Соберите бургер'

    def test_click_logout_button_show_login_page(self, login: WebDriver) -> None:                                 # выход по кнопке «Выйти» в ЛК.
        driver = login
        driver.find_element(*MainPage.PROFILE_LINK_TEXT).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ProfilePage.INFO_TEXT))
        driver.find_element(*ProfilePage.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(ProfilePage.LOGOUT_BUTTON))
        assert driver.current_url == Urls.login_page
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginPage.TITLE_TEXT)).is_displayed()
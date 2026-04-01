from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Urls, StaticUser
from locators import *


class TestLoginPage:
    def test_login_via_login_button_show_main_page(self, driver: WebDriver, registered_user: StaticUser) -> None:  # вход «Войти в аккаунт» на главной
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPage.TITLE_TEXT))
        driver.find_element(*LoginPage.EMAIL_FIELD).send_keys(registered_user.LOGIN)
        driver.find_element(*LoginPage.PASSWORD_FIELD).send_keys(registered_user.PASSWORD)
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until_not(EC.presence_of_element_located(LoginPage.LOGIN_BUTTON))
        assert driver.current_url == Urls.main_page and driver.find_element(*MainPage.ORDER_BUTTON)

    def test_login_via_profile_show_main_page(self, driver: WebDriver) -> None:                                    # вход через кнопку ЛК
        driver.find_element(*MainPage.PROFILE_LINK_TEXT).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPage.TITLE_TEXT))
        driver.find_element(*LoginPage.EMAIL_FIELD).send_keys(StaticUser.LOGIN)
        driver.find_element(*LoginPage.PASSWORD_FIELD).send_keys(StaticUser.PASSWORD)
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until_not(EC.presence_of_element_located(LoginPage.LOGIN_BUTTON))
        assert driver.current_url == Urls.main_page and driver.find_element(*MainPage.ORDER_BUTTON)

    def test_login_via_registration_page_show_main_page(self, driver: WebDriver) -> None:                          # вход через кнопку в форме регистрации
        driver.get(Urls.reg_page)
        driver.find_element(*RegPage.LOGIN_TEXT_WITH_HREF).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPage.TITLE_TEXT))
        driver.find_element(*LoginPage.EMAIL_FIELD).send_keys(StaticUser.LOGIN)
        driver.find_element(*LoginPage.PASSWORD_FIELD).send_keys(StaticUser.PASSWORD)
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until_not(EC.presence_of_element_located(LoginPage.LOGIN_BUTTON))
        assert driver.current_url == Urls.main_page and driver.find_element(*MainPage.ORDER_BUTTON)

    def test_login_via_recover_pass_page_show_main_page(self, driver: WebDriver) -> None:                          # вход через кнопку в форме восстановления пароля
        driver.get(Urls.recover_pass_page)
        driver.find_element(*LoginPage.LOGIN_TEXT_WITH_HREF).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(LoginPage.TITLE_TEXT))
        driver.find_element(*LoginPage.EMAIL_FIELD).send_keys(StaticUser.LOGIN)
        driver.find_element(*LoginPage.PASSWORD_FIELD).send_keys(StaticUser.PASSWORD)
        driver.find_element(*LoginPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until_not(EC.presence_of_element_located(LoginPage.LOGIN_BUTTON))
        assert driver.current_url == Urls.main_page and driver.find_element(*MainPage.ORDER_BUTTON)
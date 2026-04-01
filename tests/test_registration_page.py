import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Urls, User
from locators import *


class TestRegistrationPage:
    def test_successful_registration(self, driver: WebDriver) -> None:                      # успешная регистрация
        user = User.generate()
        driver.get(Urls.reg_page)
        driver.find_element(*RegPage.NAME_INPUT).send_keys(user.name)
        driver.find_element(*RegPage.EMAIL_INPUT).send_keys(user.login)
        driver.find_element(*RegPage.PASSWORD_INPUT).send_keys(user.password)
        driver.find_element(*RegPage.REGISTRATE_BUTTON).click()
        WebDriverWait(driver, 5).until_not(EC.presence_of_element_located(RegPage.REGISTRATE_BUTTON))
        assert driver.current_url == Urls.login_page
        assert driver.find_element(*LoginPage.TITLE_TEXT).is_displayed()

    
    @pytest.mark.parametrize('password', ['1', '123', '1234', '12345'])                      # некорректный пароль
    def test_incorrect_password_error(self, driver: WebDriver, password: str) -> None:
        user = User.generate()
        driver.get(Urls.reg_page)
        driver.find_element(*RegPage.NAME_INPUT).send_keys(user.name)
        driver.find_element(*RegPage.EMAIL_INPUT).send_keys(user.login)
        driver.find_element(*RegPage.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegPage.REGISTRATE_BUTTON).click()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegPage.INPUT_ERROR_TEXT)).is_displayed()
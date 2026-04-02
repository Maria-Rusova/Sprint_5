import pytest
from typing import Generator
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Urls, StaticUser
from locators import LoginPage, MainPage


@pytest.fixture
def driver() -> Generator[WebDriver, None, None]:
    driver = webdriver.Chrome()
    driver.get(Urls.main_page)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def registered_user() -> StaticUser:
    user = StaticUser.get_static()
    temp_driver = webdriver.Chrome()
    StaticUser.register(temp_driver, user)
    temp_driver.quit()
    return user


@pytest.fixture
def login(driver: WebDriver) -> WebDriver:
    driver.get(Urls.login_page)
    driver.find_element(*LoginPage.EMAIL_FIELD).send_keys(StaticUser.LOGIN)
    driver.find_element(*LoginPage.PASSWORD_FIELD).send_keys(StaticUser.PASSWORD)
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPage.ORDER_BUTTON))
    return driver
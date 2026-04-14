from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPage

class TestConstructorSection:
    def test_click_buns_scroll_to_buns(self, login: WebDriver) -> None:
        driver = login
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(MainPage.CONSTRUCTOR_LINK_TEXT)).click()
        buns_tab = wait.until(EC.element_to_be_clickable(MainPage.BUNS_TAB))
        buns_tab.click
        wait.until(EC.visibility_of_element_located(MainPage.BUNS_SECTION_HEADER))

    def test_click_sauces_scroll_to_sauces(self, login: WebDriver) -> None:
        driver = login
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(MainPage.CONSTRUCTOR_LINK_TEXT)).click()
        sauces_tab = wait.until(EC.element_to_be_clickable(MainPage.SAUCES_TAB))
        sauces_tab.click()
        wait.until(EC.visibility_of_element_located(MainPage.SAUCES_SECTION_HEADER))

    def test_click_fillings_scroll_to_fillings(self, login: WebDriver) -> None:
        driver = login
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(MainPage.CONSTRUCTOR_LINK_TEXT)).click()
        fillings_tab = wait.until(EC.element_to_be_clickable(MainPage.FILLINGS_TAB))
        fillings_tab.click()
        wait.until(EC.visibility_of_element_located(MainPage.FILLINGS_SECTION_HEADER))
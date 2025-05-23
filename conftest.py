import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pages.create_account_pages import CreateAccount
from pages.eco_friendly_pages import EcoFriendlyPage
from pages.sale_pages import SalePage
from time import sleep


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    return chrome_driver


@pytest.fixture()
def create_acc_page(driver):
    return CreateAccount(driver)

@pytest.fixture()
def create_eco_friendly_page(driver):
    return EcoFriendlyPage(driver)

@pytest.fixture()
def create_sale_page(driver):
    return SalePage(driver)
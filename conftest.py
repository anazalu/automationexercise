from selenium import webdriver
import pytest

@pytest.fixture(scope="session")
def driver():    
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def api_base_url():
    return 'https://automationexercise.com/api'

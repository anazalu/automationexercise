from selenium import webdriver
import pytest

@pytest.fixture(scope="session")
def driver():    
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

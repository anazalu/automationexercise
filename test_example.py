from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_check_title(driver):    
    assert driver is not None
    driver.get("https://www.automationexercise.com/")
    expected_title = "Automation Exercise"
    title = driver.title
    assert title.startswith("Auto")
    assert title.endswith("Exercise")
    assert title == expected_title, "Title mismatch"
    
def test_check_products_link_text(driver):
    driver.get("https://www.automationexercise.com/")
    products_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@href='/products']"))
    )
    expected_link_text_fragment = "Products"
    actual_link_text = products_link.text
    assert expected_link_text_fragment in actual_link_text, "Link text mismatch"

def test_click_products_link_and_verify_header(driver):
    driver.get("https://www.automationexercise.com/")
    products_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@href='/products']"))
    )
    products_link.click()
    all_products_header = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'All Products')]"))
    )
    actual_header_text = all_products_header.text.lower()
    expected_header_text = "All Products".lower()
    assert actual_header_text == expected_header_text, "Header text mismatch"

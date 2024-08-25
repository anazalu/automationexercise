import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.xfail
def test_check_title(driver):    
    assert driver is not None
    driver.get("https://www.automationexercise.com/")
    expected_title = "Automation Exercise"
    title = driver.title
    assert title.startswith("Auto")
    assert title.endswith("Exercise")
    assert title == expected_title, "Title mismatch"
    
@pytest.mark.xfail
def test_check_products_link_text(driver):
    driver.get("https://www.automationexercise.com/")
    products_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[@href='/products']"))
    )
    expected_link_text_fragment = "Products"
    actual_link_text = products_link.text
    assert expected_link_text_fragment in actual_link_text, "Link text mismatch"

@pytest.mark.xfail
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

@pytest.mark.xfail
def test_add_one_item_to_cart(driver):
    item_name = 'Blue Top'
    driver.get("https://www.automationexercise.com/")
    add_one_item =  WebDriverWait(driver, 10).until(
        # EC.visibility_of_element_located((By.XPATH, "//div[@class='productinfo text-center'][p='{}']/a[@class='btn btn-default add-to-cart']".format(item_name)))
        EC.visibility_of_element_located((By.XPATH, "//div[@class='productinfo text-center'][p='" + item_name + "']/a[@class='btn btn-default add-to-cart']"))
    )
    add_one_item.click()
    view_cart = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='modal-content']//div[@class='modal-body']//a[@href='/view_cart']/u"))
    )
    view_cart.click()
    find_item_in_cart = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//table[@id='cart_info_table']//tr[contains(td[@class='cart_description']//h4/a, '" + item_name + "')]"))
    )
    assert find_item_in_cart is not None, "Product '" + item_name + "' not found in the cart"

@pytest.mark.xfail
def test_add_multiple_items_to_cart(driver):
    items = ["Blue Top", "Men Tshirt", "Winter Top", "Stylish Dress"]
    driver.get("https://www.automationexercise.com/")
    
    for item in items:
        add_item_xpath = "//div[@class='productinfo text-center'][p='{}']/a[@class='btn btn-default add-to-cart']".format(item)
        add_item = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, add_item_xpath)))
        add_item.click()
        # Assuming there's a modal, click on continue shopping
        continue_shopping_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='modal-content']//div[@class='modal-footer']//button")))
        continue_shopping_button.click()

    view_cart = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='nav navbar-nav']//a[@href='/view_cart']")))
    view_cart.click()

    for item in items:
        product_in_cart = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//table[@id='cart_info_table']//tr[contains(td[@class='cart_description']//h4/a, '" + item + "')]")))
        assert product_in_cart is not None, "Product '" + item + "' not found in the cart"

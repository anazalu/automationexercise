def test001(driver):    
    assert driver is not None

    driver.get("https://www.automationexercise.com/")

    title = driver.title
    assert title.endswith("Exercise")
    assert title.startswith("Auto")
    
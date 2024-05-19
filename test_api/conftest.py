import pytest
import time

username = 'user' + str(time.time())[11:]
email = username + '@one.lv'
password = '11passWord&&'

@pytest.fixture(scope="session")
def api_base_url():
    return 'https://automationexercise.com/api'

@pytest.fixture(scope="function")
def registration_data():
    return {
        "name": username,
        "email": email,
        "password": password,
        "firstname": "",
        "lastname": "",
        "address1": "",
        "country": "",
        "zipcode": "",
        "state": "",
        "city": "",
        "mobile_number": ""}

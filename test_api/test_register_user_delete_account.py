import pytest
import requests
from test_api import conftest

def test_negative_register_without_data(api_base_url):
    endpoint = api_base_url + '/createAccount'
    response = requests.post(endpoint, timeout=30)
    assert '400' in str(response.json())
    assert 'parameter is missing' in str(response.json())

def test_negative_register_with_empty_data(api_base_url):
    endpoint = api_base_url + '/createAccount'
    empty_data = {
    }
    response = requests.post(endpoint, timeout=30, data=empty_data)
    assert '400' in str(response.json())
    assert 'parameter is missing' in str(response.json())

@pytest.mark.parametrize("text_field", ["name", "email", "password", "firstname", "lastname",
                                        "address1", "country", "zipcode", "state", "city", "mobile_number"])
def test_negative_register_without_one_text_field(api_base_url, registration_data, text_field):
    endpoint = api_base_url + '/createAccount'
    registration_data.pop(text_field)
    response = requests.post(endpoint, timeout=30, data=registration_data)
    assert '400' in str(response.json())
    assert f'{text_field} parameter is missing' in str(response.json())

def test_negative_delete_without_data(api_base_url):
    endpoint = api_base_url + '/deleteAccount'
    response = requests.delete(endpoint, timeout=30)
    assert '400' in str(response.json())
    assert 'parameter is missing' in str(response.json())

def test_negative_delete_without_email(api_base_url):
    endpoint = api_base_url + '/deleteAccount'
    data = {
        "password": conftest.password
    }
    response = requests.delete(endpoint, timeout=30, data=data)
    assert '400' in str(response.json())
    assert 'parameter is missing' in str(response.json())

def test_register_and_delete_user_account(api_base_url, registration_data):
    endpoint = api_base_url + '/createAccount'
    response = requests.post(endpoint, timeout=30, data=registration_data)
    print(registration_data["email"])
    assert '201' in str(response.json())
    assert 'User created' in str(response.json())

    response = requests.post(endpoint, timeout=30, data=registration_data)
    assert '400' in str(response.json())
    assert 'Email already exists' in str(response.json())
    
    endpoint = api_base_url + '/deleteAccount'
    data = {
        "email": conftest.email,
        "password": conftest.password
    }
    response = requests.delete(endpoint, timeout=30, data=data)
    print(conftest.email)
    assert '200' in str(response.json()), conftest.email + "==" + registration_data["email"]
    assert 'Account deleted' in str(response.json())

    response = requests.delete(endpoint, timeout=30, data=data)
    assert '404' in str(response.json())
    assert 'Account not found' in str(response.json())

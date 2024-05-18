import requests
# from registration_data import data
import time

username = 'user' + str(time.time())[11:]
email = username + '@one.lv'
password = '11passWord&&'

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

def test_negative_register_without_country(api_base_url):
    endpoint = api_base_url + '/createAccount'
    data = {
        "name": f"${username}",
        "email": f"${email}",
        "password": f"${password}",
        "firstname": "",
        "lastname": "",
        "address1": "",
        "zipcode": "",
        "state": "",
        "city": "",
        "mobile_number": ""
    }
    response = requests.post(endpoint, timeout=30, data=data)
    assert '400' in str(response.json())
    assert 'parameter is missing' in str(response.json())

def test_register_user_account(api_base_url):
    endpoint = api_base_url + '/createAccount'
    data = {
        "name": f"${username}",
        "email": f"${email}",
        "password": f"${password}",
        "firstname": "",
        "lastname": "",
        "address1": "",
        "country": "",
        "zipcode": "",
        "state": "",
        "city": "",
        "mobile_number": ""
    }
    response = requests.post(endpoint, timeout=30, data=data)
    assert '201' in str(response.json())
    assert 'User created' in str(response.json())

def test_negative_register_existing_user(api_base_url):
    endpoint = api_base_url + '/createAccount'
    data = {
        "name": f"${username}",
        "email": f"${email}",
        "password": f"${password}",
        "firstname": "",
        "lastname": "",
        "address1": "",
        "country": "",
        "zipcode": "",
        "state": "",
        "city": "",
        "mobile_number": ""
    }
    response = requests.post(endpoint, timeout=30, data=data)
    assert '400' in str(response.json())
    assert 'Email already exists' in str(response.json())

def test_negative_delete_without_data(api_base_url):
    endpoint = api_base_url + '/deleteAccount'
    response = requests.delete(endpoint, timeout=30)
    assert '400' in str(response.json())
    assert 'parameter is missing' in str(response.json())

def test_negative_delete_without_email(api_base_url):
    endpoint = api_base_url + '/deleteAccount'
    data = {
        "password": f"${password}"
    }
    response = requests.delete(endpoint, timeout=30, data=data)
    assert '400' in str(response.json())
    assert 'parameter is missing' in str(response.json())

def test_delete_user_account(api_base_url):
    endpoint = api_base_url + '/deleteAccount'
    data = {
        "email": f"${email}",
        "password": f"${password}"
    }
    response = requests.delete(endpoint, timeout=30, data=data)
    assert '200' in str(response.json())
    assert 'Account deleted' in str(response.json())

def test_negative_delete_deleted_account(api_base_url):
    endpoint = api_base_url + '/deleteAccount'
    data = {
        "email": f"${email}",
        "password": f"${password}"
    }
    response = requests.delete(endpoint, timeout=30, data=data)
    assert '404' in str(response.json())
    assert 'Account not found' in str(response.json())

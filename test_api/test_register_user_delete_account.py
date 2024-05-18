import requests
import time

username = 'user' + str(time.time())[11:]
email = username + 'one.lv'
password = '11passWord&&'

def test_register_user_account(api_base_url):
    endpoint = api_base_url + '/createAccount'
    data = {
        "name": f"${username}",
        "email": f"${email}",
        "password": f"${password}",
        "firstname": "firstname",
        "lastname": "lastname",
        "address1": "6867 jghkdghdkh",
        "country": "US",
        "zipcode": "99615",
        "state": "AK",
        "city": "Kodiak",
        "mobile_number": "207-319-1533"
    }
    response = requests.post(endpoint, timeout=30, data=data)
    assert '201' in str(response.json())
    assert 'User created' in str(response.json())

def test_delete_user_account(api_base_url):
    endpoint = api_base_url + '/deleteAccount'
    data = {
        "email": f"${email}",
        "password": f"${password}"
    }
    response = requests.delete(endpoint, timeout=30, data=data)
    assert '200' in str(response.json())
    assert 'Account deleted' in str(response.json())

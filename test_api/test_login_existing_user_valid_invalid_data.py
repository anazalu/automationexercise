import requests

def test_login_valid_data(api_base_url):
    endpoint = api_base_url + '/verifyLogin'
    data = {'email': 'alaque@gmail.com', 'password': '1userSunMay&'}
    response = requests.post(endpoint, timeout=30, data=data)
    assert response.status_code == 200
    assert 'User exists' in str(response.json())
    
def test_login_incomplete_data(api_base_url):
    endpoint = api_base_url + '/verifyLogin'
    data = {'email': 'alaque@gmail.com'}
    response = requests.post(endpoint, timeout=30, data=data)
    assert '400' in str(response.json())
    assert 'Bad request' in str(response.json())

def test_login_invalid_data(api_base_url):
    endpoint = api_base_url + '/verifyLogin'
    data = {'email': 'alaque@gmail.com', 'password': 'wrongPassword'}
    response = requests.post(endpoint, timeout=30, data=data)
    assert '404' in str(response.json())
    assert 'User not found' in str(response.json())

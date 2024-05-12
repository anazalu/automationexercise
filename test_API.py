import pytest
import requests

@pytest.fixture
def base_url():
    return 'https://automationexercise.com/api'

def test_get_all_products_list(base_url):
    endpoint = base_url + '/productsList'
    response = requests.get(endpoint, timeout=30)
    assert response.status_code == 200
    assert len(str(response.json())) != 0
    assert 'products' in response.json()
    assert 'Grunt Blue Slim Fit Jeans' in str(response.json())
    assert 'Blue Top' in str(response.json())

def test_login_valid_data(base_url):
    endpoint = base_url + '/verifyLogin'
    data = {'email': 'alaque@gmail.com', 'password': '1userSunMay&'}
    response = requests.post(endpoint, timeout=30, data=data)
    assert response.status_code == 200
    assert 'User exists' in str(response.json())
    
def test_login_incomplete_data(base_url):
    endpoint = base_url + '/verifyLogin'
    data = {'email': 'alaque@gmail.com'}
    response = requests.post(endpoint, timeout=30, data=data)
    assert '400' in str(response.json())
    assert 'Bad request' in str(response.json())

def test_login_invalid_data(base_url):
    endpoint = base_url + '/verifyLogin'
    data = {'email': 'alaque@gmail.com', 'password': 'wrongPassword'}
    response = requests.post(endpoint, timeout=30, data=data)
    assert '404' in str(response.json())
    assert 'User not found' in str(response.json())

def test_positive_post_to_search_product(base_url):
    endpoint = base_url + '/searchProduct'
    data = {'search_product': 'top'}
    response = requests.post(endpoint, timeout=30, data=data)
    assert '200' in str(response.json())
    assert 'Blue Top' in str(response.json())

def test_negative_post_to_search_product(base_url):
    endpoint = base_url + '/searchProduct'
    response = requests.post(endpoint, timeout=30)
    assert '400' in str(response.json())
    assert 'Bad request' in str(response.json())

@pytest.mark.parametrize("search_product,expected_response_code", [('top', '200'), ('', '400')])
def test_post_to_search_product(base_url, search_product, expected_response_code):
    endpoint = base_url + '/searchProduct'
    data = {'search_product': search_product}
    response = requests.post(endpoint, timeout=30, data=data)
    assert expected_response_code in str(response.json())

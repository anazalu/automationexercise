import pytest
import requests

def test_get_all_products_list(api_base_url):
    endpoint = api_base_url + '/productsList'
    response = requests.get(endpoint, timeout=30)
    assert response.status_code == 200
    assert len(str(response.json())) != 0
    assert 'products' in response.json()
    assert 'Grunt Blue Slim Fit Jeans' in str(response.json())
    assert 'Blue Top' in str(response.json())

def test_positive_post_to_search_product(api_base_url):
    endpoint = api_base_url + '/searchProduct'
    data = {'search_product': 'top'}
    response = requests.post(endpoint, timeout=30, data=data)
    assert '200' in str(response.json())
    assert 'Blue Top' in str(response.json())

def test_negative_post_to_search_product(api_base_url):
    endpoint = api_base_url + '/searchProduct'
    response = requests.post(endpoint, timeout=30)
    assert '400' in str(response.json())
    assert 'Bad request' in str(response.json())

@pytest.mark.parametrize("search_product,expected_response_code", [('top', '200'), ('', '400'), ('dress', '200')])
def test_post_to_search_product(api_base_url, search_product, expected_response_code):
    endpoint = api_base_url + '/searchProduct'
    data = {'search_product': search_product}
    response = requests.post(endpoint, timeout=30, data=data)
    assert expected_response_code in str(response.json())
    assert str.capitalize(search_product) in str(response.json())

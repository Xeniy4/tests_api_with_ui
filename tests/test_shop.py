from http.client import responses

import requests

base_url = "https://lime-shop.com/ru_ru/"



def test_add_items_in_cart():
    response = requests
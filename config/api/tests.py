from django.test import TestCase
import requests



class GetAllBookApi(TestCase):
    pass#response = requests.get('http://127.0.0.1:8000/api/')
    # print(response.json())


class GetBookIdApi(TestCase):
    pass#response = requests.get('http://127.0.0.1:8000/api/1')
    # print(response.json())


class GetUserOrdersApi(TestCase):

    HEADER = {
        "Content-Type": "application/json",
        "Authorization": "Token 620ef93843ede0c8762beb73a1d21e1e82eae480",
    }
    response = requests.get('http://127.0.0.1:8000/api/orders/', headers=HEADER)
    print(response.json())



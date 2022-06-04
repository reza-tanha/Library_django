from django.test import TestCase
import requests
import json



class GetAllBookApi(TestCase):
    pass#response = requests.get('http://127.0.0.1:8000/api/')
    # print(response.json())


class GetBookIdApi(TestCase):
    pass#response = requests.get('http://127.0.0.1:8000/api/1')
    # print(response.json())




class GetUserOrdersApi(TestCase):

    HEADER = {
        "Content-Type": "application/json",
        "Authorization": "Token 7062a10bde0cfba6b3692f8451b5f7c730a55a4e",
    }
    # response = requests.get('http://127.0.0.1:8000/api/orders/', headers=HEADER)
    # print(response.json())




class CreateUserOrderApi(TestCase):
    HEADER = {
        "Content-Type": "application/json",
        "Authorization": "Token 7062a10bde0cfba6b3692f8451b5f7c730a55a4e",
    }
    DATA = {
            "is_reserve": True,
            "user": "1",
            "book": "5"
        }
    # response = requests.post('http://127.0.0.1:8000/api/order/add/', headers=HEADER, data=json.dumps(DATA))
    # print(response.json())

class AddUserOrderApi(TestCase):
    HEADER = {
        "Content-Type": "application/json",
    }
    DATA = {
            "username": "user1",
            "email": "user1@gmail.com",
            "password": "pa55word"
        }
    # response = requests.post('http://127.0.0.1:8000/api/register/', headers=HEADER, data=json.dumps(DATA))
    # print(response.json())


class DeleteUserOrderApi(TestCase):
    HEADER = {
        "Content-Type": "application/json",
        "Authorization": "Token 7062a10bde0cfba6b3692f8451b5f7c730a55a4e",
    }

    # response = requests.delete('http://127.0.0.1:8000/api/order/delete/67', headers=HEADER)
    # print(response.json())


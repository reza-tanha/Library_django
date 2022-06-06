from rest_framework.test import APITestCase 
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
import requests
import json



class TestBookAppApi(APITestCase):
    pass

    # def test_get_all_book(self):
    #     url = reverse('api:books')
        # response = self.client.get(url)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # response = requests.get('http://127.0.0.1:8000/api/')
        # print(response.json())

    # def test_one_book(self):
    #     url = reverse('<int:pk>', kwargs={'pk':1})#args=(1,)
        # response = self.client.get(url)
        # print(response.status_code)
        # self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class GetBookIdApi(TestCase):
    pass#response = requests.get('http://127.0.0.1:8000/api/1')
    # print(response.json())




class GetUserOrdersApi(TestCase):

    HEADER = {
        "Content-Type": "application/json",
        "Authorization": "Token 620ef93843ede0c8762beb73a1d21e1e82eae480",
    }
    # response = requests.get('http://127.0.0.1:8000/api/orders/', headers=HEADER)
    # print(response.json())




class CreateUserOrderApi(TestCase):
    HEADER = {
        "Content-Type": "application/json",
        "Authorization": "Token 7062a10bde0cfba6b3692f8451b5f7c730a55a4e",
    }
    DATA = {
            "book": "7"
        }
    # response = requests.post('http://127.0.0.1:8000/api/order/add/', headers=HEADER, data=json.dumps(DATA))
    # print(response.json())


class AddUserOrderApi(TestCase):
    HEADER = {
        "Content-Type": "application/json",
    }
    DATA = {
            "username": "user2",
            "email": "user2@gmail.com",
            "password": "pa55word"
        }
    # response = requests.post('http://127.0.0.1:8000/api/register/', headers=HEADER, data=json.dumps(DATA))
    # print(response.json())


class DeleteUserOrderApi(TestCase):
    HEADER = {
        "Content-Type": "application/json",
        "Authorization": "Token 5e103c3b287aa1ef32ea8436982be9d401ccbd28",
    }

    # response = requests.delete('http://127.0.0.1:8000/api/order/delete/34', headers=HEADER)
    # print(response.json())


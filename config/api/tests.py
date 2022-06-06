from rest_framework.test import APITestCase 
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token
from order.models import Order
from book.models import Author, Genre, Book
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
User = get_user_model()





class TestApi(APITestCase):

    def setUp(self):

        self.user = User.objects.create(username='haji', email='haji@haji.com', password='password')
        self.token = Token.objects.create(user=self.user)

        self.author = Author.objects.create(name='shamlo')
        self.genre = Genre.objects.create(title='love', slug='love')

        img = SimpleUploadedFile('test.jpg', b'whatevercontentsyouwant')

        self.book = Book.objects.create(title='ayda', slug='ayda', athore=self.author,
            description='noting',photo=img,release_date=1993
            )

        self.book.save()
        self.book.genre.add(self.genre)
        self.order = Order.objects.create(user=self.user, book=self.book)


    def test_get_token(self):
        token = Token.objects.filter(user=1).first()
        self.assertEqual(self.user, token.user)


    def test_get_order(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = client.get(reverse('api:orders'))
        self.assertEqual(response.status_code,  status.HTTP_200_OK)


    def test_create_order(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {
            'book':1
        }
        response = client.post(reverse('api:order-add'), data=data, format='json')
        self.assertEqual(response.status_code,  status.HTTP_201_CREATED)


    def test_delete_order(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = client.delete(reverse('api:order-delete',args=[1,]) )
        self.assertEqual(response.status_code,  status.HTTP_204_NO_CONTENT)

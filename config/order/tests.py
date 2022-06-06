from django.test import TestCase
from book.models import Author, Genre, Book
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.authtoken.models import Token
from order.models import Order
from django.contrib.auth import get_user_model
User = get_user_model()


class OrderTestModel(TestCase):

    def setUp(self):
        self.author = Author.objects.create(name='shamlo')
        self.genre = Genre.objects.create(title='love', slug='love')
        img = SimpleUploadedFile('media/images/book/2022/06/02/ana-carani.png', b'whatevercontentsyouwant')

        self.book = Book.objects.create(
            title='ayda', slug='ayda', athore=self.author,
            description='noting', photo=img,release_date=1993
        )
        self.book.save()
        self.book.genre.add(self.genre)

        self.user = User.objects.create(username='haji', email='haji@haji.com', password='password')
        self.token = Token.objects.create(user=self.user)


    def test_create_order(self):
        if not self.book.reserve:
            self.order = Order.objects.create(user=self.user, book=self.book)
            self.assertEqual(self.order.id, 1)


    def test_delete_order(self):
        self.order = Order.objects.create(user=self.user, book=self.book)
        self.order.delete()
        self.assertNotEqual(self.order.id, 1)


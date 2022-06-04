from django.test import TestCase
from .models import Book
# Create your tests here.

class TestBook(TestCase):
    book = Book.objects.filter(reserve=True)
    # print(book)

    
from django.test import TestCase
from book.models import Author, Genre, Book
from django.core.files.uploadedfile import SimpleUploadedFile


class BookTestModel(TestCase):

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


    def test_create_book(self):
        img = SimpleUploadedFile('media/images/book/2022/06/02/ana-carani.png', b'whatevercontentsyouwant')

        self.book = Book.objects.create(
            title='ayda_2', slug='ayda_2', athore=self.author,
            description='noting_2', photo=img,release_date=1993
        )
        self.book.save()
        self.book.genre.add(self.genre)
        self.assertEqual(self.book.id, 2)


    def test_delete_book(self):
        book_delete = Book.objects.all().first()
        book_delete.delete()
        self.assertNotEqual(self.book.id, book_delete.id)

    

    
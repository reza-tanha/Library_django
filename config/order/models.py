from django.db import models
from django.contrib.auth import get_user_model
from book.models import Book

class Order(models.Model):
    USER = get_user_model()
    user = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='user_order', verbose_name='نام یوزر')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_order', verbose_name='نام کتاب')
    reserv_date = models.DateTimeField(auto_now_add=True)
    is_reserve = models.BooleanField(default=True)
    class Meta:
        ordering = ('reserv_date',)


    def __str__(self):
        return f"{self.book}"
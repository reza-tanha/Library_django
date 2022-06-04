from django.shortcuts import get_object_or_404
from django.test import TestCase
from .models import Order
from book.models import Book
from django.contrib.auth import get_user_model


class CreateOrder(TestCase):
    User = get_user_model()
    user = get_object_or_404(User, pk=1)
    book = get_object_or_404(Book, pk=5)
    if not book.reserve:
        order = Order.objects.create(user=user, book=book, is_reserve=True)
        order.save()
        # print("Create success")


class DeleteOrder(TestCase):
    User = get_user_model()
    user = get_object_or_404(User, pk=1)
    book = get_object_or_404(Book, pk=5)
    order = get_object_or_404(Order, pk=41, user=user, book=book)

    if order:
        book.reserve = False
        book.save()
        order.is_reserve = False
        order.save()
        # print("delet Success")



class GetOrderUser(TestCase):
    User = get_user_model()
    user = get_object_or_404(User, pk=1)
    orders = Order.objects.filter(user=user, is_reserve=True)
    for order in orders:
        pass
        # print(order.is_reserve)


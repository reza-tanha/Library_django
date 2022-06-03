from ast import Or
from django.shortcuts import render
from .serializer import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView ,
    RetrieveAPIView,
)
from book.models import Book
from order.models import Order


@api_view(['GET'])
def books(request):
    books = Book.objects.all()
    book_serializer = BookSerializer(books, many=True)
    return Response(book_serializer.data)


class BookDetail(RetrieveAPIView): 
    serializer_class = BookSerializer
    queryset = Book.objects.all()



@api_view(['GET'])
def orders(request):
    books = Order.objects.filter(user=request.user, book__reserve=True)
    book_serializer = BookSerializer(books, many=True)
    return Response(book_serializer.data)



from django.shortcuts import get_object_or_404
from .serializer import BookSerializer, OrderSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
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
    books = Order.objects.filter(user=request.user, is_reserve=True)
    book_serializer = OrderSerializer(books, many=True)
    return Response(book_serializer.data)


@api_view(['POST'])
def order_create(request):
    order = OrderSerializer(data=request.data)
    book = get_object_or_404(Book, pk=request.data.get("book"))
    if not book.reserve:
        if order.is_valid():
            book.reserve=True
            book.save()
            order.save()
        return Response(order.data)
    return Response("book exist")
    """
        {
            "is_reserve": true,
            "user": 1,
            "book": 5
        }
    """


@api_view(['DELETE'])
def order_delete(request, pk):
    order = get_object_or_404(Order, user=request.user, pk=pk)
    if order:
        book = Book.objects.get(pk=order.book.pk)
        book.reserve=False
        book.save()
        order.is_reserve=False
        order.save()
        return Response("order Deleted")




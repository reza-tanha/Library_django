from tokenize import Token
from django.shortcuts import get_object_or_404
from .serializer import BookSerializer, OrderSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from book.models import Book
from order.models import Order
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token


@api_view(['GET'])
@permission_classes([AllowAny])
def books(request):
    books = Book.objects.all()
    book_serializer = BookSerializer(books, many=True)
    return Response(book_serializer.data)


class BookDetail(RetrieveAPIView): 
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [AllowAny, ]



@api_view(['GET'])
def orders(request):
    books = Order.objects.filter(user=request.user, is_reserve=True)
    book_serializer = OrderSerializer(books, many=True)
    return Response(book_serializer.data)


@api_view(['POST'])
def order_create(request):

    order = OrderSerializer(data=request.data)
    if str(request.user.id) != str(request.data.get("user")):
        return Response("Unauthorized Error ",status=401)

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
        book = get_object_or_404(Book, pk=order.book.pk)
        book.reserve=False
        book.save()
        order.is_reserve=False
        order.save()
        return Response("order Deleted")


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serialize = UserSerializer(data=request.data)
    if serialize.is_valid():
        user = serialize.save()
        data = {}
        data['Token'] = Token.objects.get(user=user).key
        data['Message'] = 'Register Success'
    return Response(data)
        
    """
    {
        "username":"test",
        "email":"test@test.com",
        "password":"testtest"
    }
    """

 
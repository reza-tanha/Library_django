from rest_framework import serializers
from book.models import Book
from order.models import Order
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","email" ,"password"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_staff=True
        user.save()
        Token.objects.create(user=user)
        return user




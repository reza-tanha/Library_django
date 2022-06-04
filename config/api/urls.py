from django.urls import path
from .views import (books, BookDetail, orders, order_create, order_delete, register )
app_name = "api"

urlpatterns = [
    path('', books, name="books"),
    path('<int:pk>', BookDetail.as_view(), name="book"),\

    path('orders/', orders, name="orders"),
    path('order/add/', order_create, name="order-add"),
    path('order/delete/<int:pk>', order_delete, name="order-delete"),

    path('register/', register, name='user-register'),

    
]
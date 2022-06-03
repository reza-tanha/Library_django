from django.urls import path, include
from .views import books, BookDetail, orders, OrderDetail, order_create, order_delete
app_name = "api"

urlpatterns = [
    path('', books, name="books"),
    path('<int:pk>', BookDetail.as_view(), name="book"),\

    path('orders', orders, name="orders"),
    path('order/add', order_create, name="order-add"),
    path('order/delete/<int:pk>', order_delete, name="order-delete"),
    
    # path('orders', OrderDetail.as_view(), name="orders"),
    # path('<int:pk>', BookDetail.as_view(), name="book"),

    
]
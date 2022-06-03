from django.urls import path
from .views import orders_list, order_delete, order_create

app_name = 'order'
urlpatterns = [
    path('orders', orders_list, name='my-orders'),
    path('order_create/<int:pk>', order_create, name='create-orders'),
    path('order_delete/<int:pk>', order_delete, name='del-orders'),

]
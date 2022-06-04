from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls', namespace='book')),
    path('order/', include('order.urls', namespace='order')),
    path('api/', include('api.urls', namespace="api")),
]

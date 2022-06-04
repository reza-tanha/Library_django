from operator import imod
from django.urls import path
from .views import Home, book_detail
from django.conf import settings
from django.conf.urls.static import static

app_name = 'book'
urlpatterns = [
    path('', Home.as_view(), name='books'),
    path('book/<int:pk>', book_detail, name='book-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

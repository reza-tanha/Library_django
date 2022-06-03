from django.urls import path, include
from .views import books, BookDetail
app_name = "api"

urlpatterns = [
    path('', books, name="books"),
    path('<int:pk>', BookDetail.as_view(), name="book"),
]
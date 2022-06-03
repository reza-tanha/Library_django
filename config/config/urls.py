from django.contrib import admin
from django.urls import path, include

# from rest_framework_swagger.views import get_swagger_view
# schema_view = get_swagger_view(title='Pastebin API')

# from rest_framework.schemas import get_schema_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls', namespace='book')),
    path('order/', include('order.urls', namespace='order')),
    path('api/', include('api.urls', namespace="api")),

]

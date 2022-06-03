import imp
from django.contrib import admin

from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user',"book","reserv_date", 'is_reserve')
    list_filter = ('user', 'book', 'is_reserve')



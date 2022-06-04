import imp
from django.contrib import admin
from .models import Order



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id','user',"book","reserv_date", 'is_reserve', )
    list_filter = ('user', 'book', 'is_reserve')
    list_editable = ['book','user']
    list_display_link = ['order_id'],

    def order_id(self, record):
        return record.id
    

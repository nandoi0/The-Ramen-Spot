from django.contrib import admin
from .models import Customer,  Products, Category, Order, OrderItem, ShippingAddress

# Register your models here.
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
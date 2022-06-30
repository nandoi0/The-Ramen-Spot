from django.contrib import admin
from .models import Meals, Category, OrderModel

# Register your models here.
admin.site.register(Meals)
admin.site.register(Category)
admin.site.register(OrderModel)
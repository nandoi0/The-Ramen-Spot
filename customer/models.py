
from django.db import models

# Create your models here.
class Meals(models.Model):
   name = models.CharField(max_length=50)
   description = models.TextField(max_length=500)
   image = models.ImageField(upload_to= 'IMG/')
   price = models.DecimalField(max_digits=5, decimal_places=2)
   category = models.ManyToManyField('Category', related_name='item')

   def __str__(self):
      return self.name

class Category(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
       return self.name

class OrderModel(models.Model):
   created_on = models.DateTimeField(auto_now_add=True)
   price = models.DecimalField(max_digits=7, decimal_places=2)
   items = models.ManyToManyField('Meals', related_name='order')

   def __str__(self):
       return f'Order: {self.created_on.strftime("%b %d %I: %M ")}'
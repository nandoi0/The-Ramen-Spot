from django.db import models
from django.contrib.auth.models import User

# Create your models here. Models are objects in python that manage data and structure of that data. 
# Here we see different fields user, name, and email that create the object "customer".
#These objects are created on the backend in the admin panel and allow us to create instances of each obj.


class Customer(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
   name = models.CharField(max_length=200, null=True)
   email = models.CharField(max_length=200, null=True)

#the def str method allows you to return the object by the properties set in that object "name"

   def __str__(self):
      return self.name

class Products(models.Model):
   name = models.CharField(max_length=200, null=True)
   description = models.TextField(max_length=500)
   price = models.FloatField()
   dinein = models.BooleanField(default=False, null=True, blank=False)
   image = models.ImageField(null=True, blank=True)
   category = models.ManyToManyField('Category', related_name='item')

   def __str__(self):
      return self.name
   
   @property
   def imageURL(self):
      try:
         url = self.image.url
      except:
         url = ''
      return url


class Category(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name

class Order(models.Model):
   customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
   date_ordered = models.DateTimeField(auto_now_add=True)
   complete = models.BooleanField(default=False, null=True, blank=False)
   transaction_id = models.CharField(max_length=200, null=True)

   def __str__(self):
      return str(self.id)

   @property
   def delivery(self):
       delivery = False
       orderitems = self.orderitem_set.all()
       for i in orderitems:
         if i.products.dinein == False:
            delivery = True
       return delivery
       

   @property
   def cart_total(self):
      orderitems = self.orderitem_set.all()
      total = sum([item.get_total for item in orderitems])
      return total 

   @property
   def cart_items(self):
      orderitems = self.orderitem_set.all()
      total = sum([item.quantity for item in orderitems])
      return total 


class OrderItem(models.Model):
   products = models.ForeignKey(Products, on_delete=models.SET_NULL, blank=True, null=True)
   order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
   quantity = models.IntegerField(default=0, null=True, blank=True)

   @property
   def get_total(self):
      total = self.product.price * self.quantity
      return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address
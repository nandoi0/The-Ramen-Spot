from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views import View
from django.http import JsonResponse
import json

from customer.models import *


class HomePageView(TemplateView):
    template_name = 'customer/home.html'

#class ProductListView(ListView):
#    model = Products
 #   template_name = 'customer/menu.html'
 #   context_object_name = 'products'

def menu(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.cart_items
	else:
	
		items = []
		order = {'cart_total':0, 'cart_items':0, 'delivery': False}
		cartItems = order['cart_items']

	products = Products.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'customer/menu.html', context)


def restaurantCart(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.cart_items
	else:
	
		items = []
		order = {'cart_total':0, 'cart_items':0, 'delivery': False}
		cartItems = order['cart_items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'customer/cart.html', context)

def restaurantCheckout(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.cart_items
	else:
		
		items = []
		order = {'cart_total':0, 'cart_items':0, 'delivery': False}
		cartItems = order['cart_items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'customer/checkout.html', context)

def itemUpdate(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product', productId)

	customer = request.user.customer
	product = Products.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)
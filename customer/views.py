from unicodedata import category
from urllib import request
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

from customer.models import Meals, OrderModel

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'customer/home.html'

class AboutPageView(TemplateView):
    template_name = 'customer/about.html'

class OrderPageView(View):
 def get(self, request, *args, **kwargs):
     appetizer = Meals.objects.filter(category__name__contains='Appetizer')
     ramen = Meals.objects.filter(category__name__contains='Ramen')
     drinks = Meals.objects.filter(category__name__contains='Drink')


     context = {
        'appetizer': appetizer,
        'ramen': ramen,
        'drinks': drinks,
     }

     return render(request, 'customer/order.html', context)
 
 def post(self, request, *args, **kwargs):
     order_items = {
        'items': []
     }

     items = request.POST.getlist('items[]')

     for item in items:
        menu_item = Meals.objects.get(pk__contains=int(item))
        item_data = {
            'id': menu_item.pk,
            'name': menu_item.name,
            'price': menu_item.price
        }

        order_items['items'].append(item_data)

        price = 0
        items_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(price=price)
        order.items.add(*item_id)

        context = {
            'items': order_items['items'],
            'price': price
        }

        return render(request, 'customer/order_confirmation.html', context)
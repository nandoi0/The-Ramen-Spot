from django.urls import path
from .views import HomePageView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    #path('<int:pk>/', ProductListView.as_view(), name='menu'),
    path('menu/', views.menu, name="menu"),
    path('restaurantCart/', views.restaurantCart, name="cart"),
    path('restaurantCheckout/', views.restaurantCheckout, name="checkout"),
    path('update_item/', views.itemUpdate, name="update_item"),
    
]
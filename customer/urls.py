from django.urls import path
from .views import HomePageView, MenuPageView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('view/', MenuPageView.as_view(), name='view'),
    #path('<int:pk>/', ProductListView.as_view(), name='menu'),
    path('menu/', views.menu, name="menu"),
    path('restaurantCart/', views.restaurantCart, name="cart"),
    path('restaurantCheckout/', views.restaurantCheckout, name="checkout"),
    path('update_item/', views.itemUpdate, name="update_item"),
    
]
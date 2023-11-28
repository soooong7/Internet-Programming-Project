from django.urls import path
from . import views
from .views import products_list, ProductsList

urlpatterns = [
    path('', ProductsList.as_view(), name='productspost_list'),
    path('products/', products_list, name='products_list'),
]
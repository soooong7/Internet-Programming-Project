# from django.shortcuts import render
from django.views.generic import ListView
from .models import ProductsPost
class ProductsList(ListView):
    model = ProductsPost
    ordering = '-pk'

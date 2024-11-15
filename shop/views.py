from django.shortcuts import render

from .models import Category, Product, Order
from rest_framework.generics import ListCreateAPIView

class CategoryView(ListCreateAPIView):
    pass
    
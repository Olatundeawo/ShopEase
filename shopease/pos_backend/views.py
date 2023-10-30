from django.shortcuts import render
from rest_framework import generics
from . models import Customer, Product, OrderItem
from . serializers import CustomerSerializer, ProductSerializer, OrderItemSerializer



# Create your views here.
class CustomerList(generics.ListCreateAPIView):
    """Class that create view for customer model"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    """Class for retiriving, deleeting and update the api"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
    

class ProductList(generics.ListCreateAPIView):
    """Class that create view for product model"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """Class for retiriving, deleeting and update the api"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    
    
class OrderItemList(generics.ListCreateAPIView):
    """Class that create view for order item model"""
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """Class for retiriving, deleeting and update the api"""
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


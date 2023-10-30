from rest_framework import serializers
from . models import Customer, Product, OrderItem

class CustomerSerializer(serializers.ModelSerializer):
    """Class that convert the customer models to an api"""
    class Meta:
        model = Customer
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    """Class that convert the product models to an api"""
    class Meta:
        model = Product
        fields = '__all__'
        
class OrderItemSerializer(serializers.ModelSerializer):
    """Class that convert the orderitem models to an api"""
    class Meta:
        model = OrderItem
        fields = '__all__'
        
    
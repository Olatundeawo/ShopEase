from django.contrib import admin
from . models import Customer, Product, OrderItem

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Registering the customer model"""
    list_display = ['name', 'email', 'phone']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Registering the product model"""
    list_display = ['name', 'description',
                    'price', 'stock_quantity']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """Registering the orderitem model"""
    list_display = ['product', 'customer', 'quantity', 
                    'date_added']
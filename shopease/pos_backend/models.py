from django.db import models

# Create your models here.

class Product(models.Model):
    """Class model for product"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    """Class model for customers information"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class OrderItem(models.Model):
    """class model for customer order"""
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.product)
    
    
    
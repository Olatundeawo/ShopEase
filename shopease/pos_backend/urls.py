from django.urls import path
from . import views

urlpatterns = [
        path('products', views.ProductList.as_view(), name='product-list'),
        path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
        path('customers', views.CustomerList.as_view(), name='customer-list'),
        path('products/<int:pk>/', views.CustomerDetail.as_view(), name='customer-detail'),
        path('orderitem', views.OrderItemList.as_view(), name='order-list'),
        path('orderitem/<int:pk>/', views.OrderItemDetail.as_view(), name='order-detail'),
]

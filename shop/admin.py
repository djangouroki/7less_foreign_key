from django.contrib import admin
from .models import Category, Customer, Product, Order, OrderItems

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItems)

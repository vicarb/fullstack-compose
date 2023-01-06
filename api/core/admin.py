from django.contrib import admin
from .models import Product, ProductImages, Order, Delivery
# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Order)
admin.site.register(Delivery)
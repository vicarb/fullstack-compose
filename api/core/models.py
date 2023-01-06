from django.db import models
import random
from django.contrib.postgres.fields import ArrayField
# Create your models here.

def random_string():
      return str(random.randint(1000000, 99999999))

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to ='uploads/', blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)

class ProductImages(models.Model):
    producto = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to ='uploads/', blank=True, null=True)


class Order(models.Model):
    items = ArrayField(ArrayField(models.CharField(max_length=1000, blank=True)), blank=True, null=True)
    session_id = models.CharField(blank=True, null=True, max_length=100)
    token_ws = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=500, blank=True, null=True)
    total_price = models.IntegerField(blank=True, null=True)

class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    mail = models.EmailField(max_length = 254, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)
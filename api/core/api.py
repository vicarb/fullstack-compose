
from ninja import NinjaAPI
from core.models import Product, Order, Delivery, ProductImages
from typing import List
from core.schema import ProductSchema, OrderSchema, DeliverySchema, ProductImagesSchema, NotFoundSchema
#from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions
#from transbank.common.integration_type import IntegrationType
from django.shortcuts import get_object_or_404





#Init ninja API

api = NinjaAPI()

@api.get("/hello")
def hello(request):
    return "Hello world"

# commerce_code = '597043568497'
# api_key = '42bdb1c2d4175e67bc45257ac14c03e7'
# return_url = "http://127.0.0.1:3000/exito"
# tx = Transaction(WebpayOptions(commerce_code, api_key, IntegrationType.LIVE))


@api.get("/products", response=List[ProductSchema])
def products(request):
    products = Product.objects.all()
    return Product.objects.all()


@api.get("/products/{product_id}", response={200:ProductSchema, 404:NotFoundSchema})
def producto(request, product_id: int):
    try:
        product = Product.objects.get(pk=product_id)
        return 200, product
    except Product.DoesNotExist as e:
        return 404, {"message": "Product doesn't exist"}


@api.get("/products-images", response=List[ProductImagesSchema])
def products_images(request):
    products_images = ProductImages.objects.all()
   
    return ProductImages.objects.all()


@api.get("/products-images/sorted/{product_id}", response=List[ProductImagesSchema])
def productsimgfilt(request, product_id: int):
    try:
        product_img = ProductImages.objects.filter(product_id=product_id)
        return 200, product_img
    except ProductImages.DoesNotExist as e:
        return 404, {"message": "Product doesnt exist"}

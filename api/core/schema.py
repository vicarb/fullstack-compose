from core.models import Product, Order, Delivery, ProductImages
from ninja import Schema, ModelSchema

class ProductSchema(ModelSchema):
    class Config:
        model = Product
        model_fields = '__all__'

class OrderSchema(ModelSchema):
    class Config:
        model = Order
        model_fields = '__all__'
        
class DeliverySchema(ModelSchema):
    class Config:
        model = Delivery
        model_fields = '__all__'

class ProductImagesSchema(ModelSchema):
    class Config:
        model = ProductImages
        model_fields = '__all__'

class NotFoundSchema(Schema):
    message: str
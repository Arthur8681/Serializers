from rest_framework.serializers import ModelSerializer
from .models import *

class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name', 'country']

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'manufacturer']
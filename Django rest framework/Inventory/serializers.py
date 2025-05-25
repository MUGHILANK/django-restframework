from rest_framework import serializers
from .models import *

class Product_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class Product_Serializers2(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["product_name"]
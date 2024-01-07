from rest_framework import serializers
from shop.models import Product, Manufacture


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ManufactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacture
        fields = "__all__"

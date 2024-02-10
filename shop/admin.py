from django.contrib import admin

from shop.models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacture", "collection", "price", "quantity"]


@admin.register(Manufacture)
class ManufactureAdmin(admin.ModelAdmin):
    list_display = ["brand", "country"]


@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = [
        "product",
        "mechanism_type",
        "waterproof",
        "weight",
        "case_material",
        "bracelet_material",
        "glass",
    ]

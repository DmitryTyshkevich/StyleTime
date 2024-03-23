from django.contrib import admin

from orders.models import *


# admin.site.register(Order)
# admin.site.register(OrderItem)

class CartTabAdmin(admin.TabularInline):
    model = OrderItem
    fields = "order", "product", "quantity", "price"
    # readonly_fields = ("price",)
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "last_name", "address", "city"]
    inlines = [CartTabAdmin]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "price", "quantity"]

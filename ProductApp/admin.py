from django.contrib import admin

# Register your models here.
from .models import Product,Order,OrderItem,Cart,CartItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
     list_display = ('P_name', 'Price', 'Quantity')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'ordered_at')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')
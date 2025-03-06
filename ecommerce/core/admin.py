from django.contrib import admin
from .models import Address, Product, CartItem, Order, ProductCategory, Payment, UserProfile

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'address', 'city', 'state', 'pincode']

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'description', 'price', 'discounted_price']

@admin.register(CartItem)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'get_products', 'get_total_quantity', 'status', 'ordered_at']

    def get_products(self, obj):
        return ", ".join([p.name for p in obj.products.all()])
    get_products.short_description = 'Products'

    def get_total_quantity(self, obj):
        return sum(1 for p in obj.products.all())
    get_total_quantity.short_description = 'Total Quantity'

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'payment_status', 'payment_method', 'transaction_id', 'paid_at']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'phone', 'address', 'city', 'state', 'pincode']



from django.contrib import admin
from .models import Product, Category, Cart, Order, OrderItem, Profile

# Register Product model
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'created_at', 'updated_at')
    list_filter = ('category', 'price')
    search_fields = ('name', 'description')

admin.site.register(Product, ProductAdmin)

# Register Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)

# Register Cart model
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    search_fields = ('user__username',)

admin.site.register(Cart, CartAdmin)

# Register Order model
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'total_amount', 'created_at')
    list_filter = ('status',)
    search_fields = ('user__username', 'status')

admin.site.register(Order, OrderAdmin)

# Register OrderItem model
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    search_fields = ('order__id', 'product__name')

admin.site.register(OrderItem, OrderItemAdmin)

# Register Profile model (Custom user profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address')
    search_fields = ('user__username',)

admin.site.register(Profile, ProfileAdmin)




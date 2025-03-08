from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),

    # Product Listings
    path('products/', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    
    # Categories
    path('category/<int:category_id>/', views.product_by_category, name='product_by_category'),
    path('makeup/', views.makeup, name='makeup'),
    path('skincare/', views.skincare, name='skincare'),
    path('haircolour/', views.haircolour, name='haircolour'),
    
    # Cart
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    # Checkout
    path('checkout/', views.checkout, name='checkout'),
    path('order/place/', views.place_order, name='place_order'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
     path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
     path('search_result/', views.search_result, name='search_result'),
    
    # User Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('forget-password/', views.forget_password, name='forget_password'),

    # Password Reset
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', views.password_reset_complete, name='password_reset_complete'),

    # Order and Payment
    path('order/<int:id>/', views.order_detail, name='order_detail'),
    path('payment/', views.payment, name='payment'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/failed/', views.payment_failed, name='payment_failed'),
]



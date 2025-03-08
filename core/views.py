from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm, CartUpdateForm, OrderForm, ProfileForm
from .models import Product, Category, Cart, CartItem, Order, Profile
from django.contrib.auth.decorators import login_required

# Home Page
def home(request):
    products = Product.objects.all()  # Get all products to display on the homepage
    return render(request, 'core/home.html', {'products': products})

# Product List
def product_list(request):
    products = Product.objects.all()  # Get all products
    return render(request, 'core/product_list.html', {'products': products})

# Product Detail
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'core/product_detail.html', {'product': product})

# Category Filter (Products by Category)
def product_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'core/product_by_category.html', {'products': products, 'category': category})

# User Registration
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'core/register.html', {'form': form})

# User Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'core/login.html', {'error': 'Invalid credentials'})
    return render(request, 'core/login.html')

# User Logout
def logout_view(request):
    logout(request)
    return redirect('home')

# Profile Page
@login_required
def profile(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'core/profile.html', {'profile': user_profile})

# Add Product to Cart
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)  # Get or create cart for user
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1  # Increase quantity if item already in the cart
        cart_item.save()

    return redirect('view_cart')

# View Cart
@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()  # Get all items in the cart
    return render(request, 'core/view_cart.html', {'cart_items': cart_items})

# Update Cart Item Quantity
@login_required
def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if request.method == 'POST':
        form = CartUpdateForm(request.POST)
        if form.is_valid():
            cart_item.quantity = form.cleaned_data['quantity']
            cart_item.save()
            return redirect('view_cart')
    else:
        form = CartUpdateForm(initial={'quantity': cart_item.quantity})
    return render(request, 'core/update_cart_item.html', {'form': form, 'cart_item': cart_item})

# Remove Item from Cart
@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('view_cart')

# Checkout Page
@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    total_amount = sum(item.get_total_price() for item in cart_items)

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.user = request.user
            order.total_amount = total_amount
            order.save()

            # Create order items from the cart
            for item in cart_items:
                order_form.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.product.price)

            # Clear the cart
            cart.items.all().delete()
            return redirect('payment')
    else:
        order_form = OrderForm()

    return render(request, 'core/checkout.html', {'order_form': order_form, 'cart_items': cart_items, 'total_amount': total_amount})

# Place Order
@login_required
def place_order(request):
    # Process the order here and create an order in the database
    pass  # Implement according to your business logic

# Payment Page
@login_required
def payment(request):
    return render(request, 'core/payment.html')

# Payment Success Page
@login_required
def payment_success(request):
    return render(request, 'core/payment_success.html')

# Payment Failed Page
@login_required
def payment_failed(request):
    return render(request, 'core/payment_failed.html')

# Password Reset Views
def password_reset(request):
    # Implement password reset functionality here
    pass

def password_reset_done(request):
    # Implement password reset done view here
    pass

def password_reset_confirm(request, uidb64, token):
    # Implement password reset confirm view here
    pass

def password_reset_complete(request):
    # Implement password reset complete view here
    pass


# Order Detail View
@login_required
def order_detail(request, id):
    # Get the order by ID
    order = get_object_or_404(Order, id=id, user=request.user)
    # Get the items associated with this order
    order_items = order.items.all()
    # Calculate the total amount for the order
    total_amount = sum(item.get_total_price() for item in order_items)

    return render(request, 'core/order_detail.html', {
        'order': order,
        'order_items': order_items,
        'total_amount': total_amount
    })
# in views.py
from django.shortcuts import render

def makeup(request):
    # Your view logic here
    return render(request, 'core/makeup.html')


def skincare(request):
    # Your view logic here
    return render(request, 'core/skincare.html')

def haircolour(request):
    # Your view logic here
    return render(request, 'core/haircolour.html')


def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')

def forget_password(request):
    return render(request, 'core/forget_password.html')

def search_result(request):
    return render(request, 'core/search_result.html')
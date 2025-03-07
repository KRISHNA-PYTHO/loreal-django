from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Address, Order, CartItem, Payment, UserProfile, CartItem, ProductCategory
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import AddressForm

# Home Page
def home(request):
    products = Product.objects.all()
    return render(request, 'core/home.html', {'products': products})
#about
def about(request):
    return render(request, 'core/about.html')


# Contact Page
def contact(request):
    return render(request, 'contact.html')

# User Authentication
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

# Product Views
def product_list(request, category):
    products = Product.objects.filter(category=category)
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

# CartItem Management
@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'core/view_cart.html', {'cart_items': cart_items})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(CartItem, id=cart_id)
    cart_item.delete()
    return redirect('cart')

# Checkout and Order Management
@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_amount = sum(item.product.discounted_price * item.quantity for item in cart_items)
    order = Order.objects.create(user=request.user, total_amount=total_amount)
    order.products.set([item.product for item in cart_items])
    cart_items.delete()
    return redirect('order_summary')

@login_required
def order_summary(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order.html', {'orders': orders})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_history.html', {'orders': orders})

@login_required
def place_order(request):
    return render(request, 'place_order.html')

# Payment Views
@login_required
def payment(request):
    return render(request, 'payment.html')

@login_required
def payment_success(request):
    return render(request, 'payment_success.html')

@login_required
def payment_failed(request):
    return render(request, 'payment_failed.html')

# User Profile
@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'profile.html', {'profile': profile})

# Reset Password
def reset_password(request):
    return render(request, 'reset_password.html')

# Skincare Category
def skincare(request):
    skincare_categories = ProductCategory.objects.all()
    return render(request, 'core/skincare.html', {'skincare_categories': skincare_categories})

def haircolour(request):
    hair_categories = ProductCategory.objects.all()
    return render(request, 'core/haircolour.html', {'hair_categories': hair_categories})

def makeup(request):
    make_categories = ProductCategory.objects.all()
    return render(request, 'core/makeup.html', {'hair_categories': make_categories})

# Address Form Handling
def address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('address')
    else:
        form = AddressForm()
    return render(request, 'core/address.html', {'form': form})




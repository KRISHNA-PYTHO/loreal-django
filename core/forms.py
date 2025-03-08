from django import forms
from .models import Product, Order, Cart, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# User Registration Form
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

# User Login Form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

# Cart Update Form
class CartUpdateForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 70px;'}))

# Profile Form
class ProfileForm(forms.ModelForm):
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address', 'rows': 3}))

    class Meta:
        model = Profile
        fields = ['phone', 'address']

# Order Form
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['shipping_address', 'payment_method']

    shipping_address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Shipping Address', 'rows': 3}))
    payment_method = forms.ChoiceField(choices=[('Credit Card', 'Credit Card'), ('PayPal', 'PayPal')], widget=forms.Select(attrs={'class': 'form-control'}))

# Product Filter Form (for search and filter)
class ProductFilterForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Product.objects.all(), empty_label="All Categories", required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    min_price = forms.DecimalField(min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Min Price'}))
    max_price = forms.DecimalField(min_value=0, required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Max Price'}))



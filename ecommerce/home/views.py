# Create your views here.

from django.shortcuts import render,redirect
from .models import Product, Carousel

def home(request):
    products = Product.objects.all()
    carousels = Carousel.objects.all()

    context = {
        'products': products,
        'carousels': carousels
    }
    return render(request, 'home/product_list.html', context)

    # --------------------
def signup(request):
    return render(request, 'home/signup.html')

def login(request):
    return render(request, 'home/login.html')

# -----------------------

def about(request):
    return render(request, 'home/about.html')

def cart(request):
    return render(request, 'home/cart.html')
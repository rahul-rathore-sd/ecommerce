from django.contrib import admin

# Register your models here.
from .models import Product, Carousel

admin.site.register(Product)

admin.site.register(Carousel)
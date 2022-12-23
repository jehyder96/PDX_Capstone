from django.shortcuts import render
from .models import * #importing all models

def home(request):
    return render(request, 'pages/home.html')

def cart(request):
    return render(request, 'pages/cart.html')

def checkout(request):
    return render(request, 'pages/checkout.html')

def about(request):
    return render(request, 'pages/about.html')

def products(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'pages/products.html', context)

def hair(request):
    hair_products = Product.objects.filter(product_type='Hair')
    context = {'hair':hair_products}
    return render(request, 'pages/hair.html', context)

def skin(request):
    skin_products = Product.objects.filter(product_type='Skin')
    context = {'skin':skin_products}
    return render(request, 'pages/skin.html', context)

def wash(request):
    wash_products = Product.objects.filter(product_type='Wash')
    context = {'wash':wash_products}
    return render(request, 'pages/wash.html', context)
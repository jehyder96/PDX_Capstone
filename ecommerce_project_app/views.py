from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def cart(request):
    return render(request, 'pages/cart.html')

def checkout(request):
    return render(request, 'pages/checkout.html')

def about(request):
    return render(request, 'pages/about.html')

def products(request):
    return render(request, 'pages/products.html')

def hair(request):
    return render(request, 'pages/hair.html')

def skin(request):
    return render(request, 'pages/skin.html')

def wash(request):
    return render(request, 'pages/wash.html')
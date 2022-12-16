from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def cart(request):
    return render(request, 'pages/cart.html')

def checkout(request):
    return render(request, 'pages/checkout.html')
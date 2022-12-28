from django.shortcuts import render
from .models import * #importing all models

def home(request):
    return render(request, 'pages/home.html')

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer # to access the one to one relationship
        order, created = Order.objects.get_or_create(customer=customer, complete=False) #create it or find the item
        items = order.orderitem_set.all()
    else:
        items = [] #if we don't have it we don't start the loop
        order ={'get_cart_total':0, 'get_cart_items':0}
    return render(request, 'pages/cart.html')

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_total': 0}
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


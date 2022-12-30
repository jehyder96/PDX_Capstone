from django.shortcuts import render
from django.http import JsonResponse #used to return a type of message
from .models import * #importing all models
import json

def home(request):
    # items = Order.get_cart_total(self)
    # print(items)
    return render(request, 'pages/home.html')

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer # to access the one to one relationship
        order, created = Order.objects.get_or_create(customer=customer, complete=False) #create it or find the item
        # items = order.orderitem_set.all()
        items = OrderItem.objects.all()
        cartItems = order.get_cart_items
        print(items)
        context = {'items': items}
        return render(request, 'pages/cart.html', context)
    else:
        items = [] #if we don't have it we don't start the loop
        order ={'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
        return render(request, 'pages/cart.html')

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
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

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return sonResponse('Item was added', safe=False)
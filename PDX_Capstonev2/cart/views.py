from django.shortcuts import render
from .cart import Cart
from ecommerce_app.models import Product
from django.shortcuts import get_object_or_404 #get a product object and if it doesn't exist, return error 404 not found
from django.http import JsonResponse

def cart_summary(request):

    cart = Cart(request)

    return render(request, 'cart/cart-summary.html', {'cart':cart})

def cart_add(request):

    cart = Cart(request)

    if request.POST.get('action') == 'post':

        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        product = get_object_or_404(Product, id=product_id) #we want to get an object from the model product from the ajax request
        cart.add(product=product, product_qty=product_quantity)

        cart_quantity = cart.__len__()

        response = JsonResponse({'qty': cart_quantity})

        return response

def cart_delete(request):

    cart = Cart(request)

    if request.POST.get('action') == 'post':

        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        cart_quantity = cart.__len__() #getting the cart quantity
        cart_total = cart.get_total()
        response = JsonResponse({'qty':cart_quantity, 'total':cart_total})
        return response

def cart_update(request):

    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        # creating the function
        cart.update(product=product_id, qty=product_quantity)
        #updating the total number of products in the shopping cart
        cart_quantity = cart.__len__()
        cart_total = cart.get_total()
        response = JsonResponse({'qty':cart_quantity, 'total':cart_total})
        return response

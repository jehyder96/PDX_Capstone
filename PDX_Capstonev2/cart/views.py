from django.shortcuts import render
from .cart import Cart
from ecommerce_app.models import Product
from django.shortcuts import get_object_or_404 #get a product object and if it doesn't exist, return error 404 not found

def cart_summary(request):
    return render(request, 'cart/cart-summary.html')

def cart_add(request):

    cart = Cart(request)

    if request.POST.get('action') == 'POST':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        product = get_object_or_404(Product, id=product_id) #we want to get an object from the model product from the ajax request
        cart.add(product=product, product_qty=product_quantity)

def cart_delete(request):

    pass

def cart_update(request):

    pass
# Create your views here.

from ecommerce_app.models import Product
from decimal import Decimal

class Cart():

    def __init__(self, request):
#if someone has never been to our ecommerce store, this will create a session for them
        self.session = request.session
        # returning user- obtain their existing session 
        cart = self.session.get('session_key')
        # new user - generate a new session
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        
        self.cart = cart
    
    def add(self, product, product_qty):

        product_id = str(product.id) #only want the user to change the product quantity
        if product_id in self.cart: #if product is in the cart, it can only modify the quantity
            self.cart[product_id]['qty'] = product_qty
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': product_qty}

        self.session.modified = True #telling Django that the session has been modified

    #function to count all items in the cart class
    def __len__(self):
        return sum(item['qty'] for item in self.cart.values()) #the .values method gets the total items in shopping cart

    #to iterate through all the products of the shopping cart

    def __iter__(self):
        all_products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=all_products_ids)#to verify what is in the users cart
        cart = self.cart.copy() #copy an instance of the session data
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total'] = item['price'] * item['qty']

        yield item #pauses the execution but delivers the object
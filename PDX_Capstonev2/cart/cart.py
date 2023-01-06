from ecommerce_app.models import Product

class Cart():

    def __init__(self, request):
#if someone has never been to our ecommerce store, this will create a session for them
        self.session = request.session 
        cart = self.session.get('session_key')
# new user - generate a new session
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        
        self.cart = {}
    
    def add(self, product, product_qty):

        product_id = str(product.id)
        if product_id in self.cart: #if product is in the cart, it can only modify the quantity
            self.cart[product_id]['qty'] = product_qty
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': product_qty}

        self.session.modified = True
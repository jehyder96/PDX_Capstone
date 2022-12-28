from django.db import models
from django.contrib.auth.models import User #default Django user models


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE) #user can only have one customer and vice versa
    name = models.CharField(max_length=150, null=True)
    email = models.EmailField(max_length=200, null=True)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    product_type = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True) #if a customer gets deleted, it only sets the customer value to Null
    order_placed = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False) #if complete is false, the customer can continue adding items
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    def get_cart_total(self): #total of the cart value
        orderitems = self.orderitem_set.all()
        total = sum([items.get_total for item in orderitems])
        return total
        
    def get_cart_items(self): #items in the cart
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    order_added = models.DateTimeField(auto_now_add=True)

    def get_total(self): #method to calculate tota value of order item
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True) #attaching to a customer and an order
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True) #used to validate the order data
    address = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=30, null=False)
    zipcode = models.CharField(max_length=15, null=False)
    order_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
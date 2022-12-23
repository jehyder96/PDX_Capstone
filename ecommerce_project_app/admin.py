from django.contrib import admin

from .models import *
#the items below are visable to see in the admin panel
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
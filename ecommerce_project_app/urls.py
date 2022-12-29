from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='checkout'),
    path('products/', views.products, name='products'),
    path('skin/', views.skin, name='skin'),
    path('wash/', views.wash, name='wash'),
    path('hair/', views.hair, name='hair')
]
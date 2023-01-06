from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home.html'),
    # path('hair/', views.hair, name = 'hair.html'),
    # path('soap/', views.soap, name = 'soap.html'),
    # path('exfoliate/', views.exfoliate, name = 'exfoliate.html'),
    # Individual product
    path('product/<slug:product_slug>/', views.product_info, name='product-info'),
    # Individual category
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),
]
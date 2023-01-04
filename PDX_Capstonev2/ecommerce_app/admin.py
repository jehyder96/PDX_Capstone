from django.contrib import admin

# Register your models here.

from . models import Category, Cart, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name',)}
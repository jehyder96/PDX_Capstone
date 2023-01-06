from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse #allows us to print out custom urls


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):

        return self.name
    
    def get_absolute_url(self):
        return reverse('list-category', args=[self.slug])

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return f'{self.name} {self.price} {self.image}'

    def get_absolute_url(self):

        return reverse('product-info', args=[self.slug])
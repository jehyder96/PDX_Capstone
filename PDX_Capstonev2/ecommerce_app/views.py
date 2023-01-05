from django.shortcuts import render
from . models import Category, Product
# from django.shortcuts import get_object_or_404

def home(request):
    all_products = Product.objects.all()

    context = {'all_products': all_products}

    return render(request, 'pages/home.html', context)

def categories(request):

    all_categories = Category.objects.all()
    return {'all_categories': all_categories}

def get_absolute_url(self):
    return reverse('product-info', args=[self.slug])

# def product_info(request):

#     product = get_object_or_404(Product, slug=slug)

#     context = {'product': product}

#     return render(request, 'pages/hair.html', context)
# Create your views here.

def hair(request):
    all_products = Product.objects.filter(name='Organic Shampoo')
    context = {'product': all_products}
    return render(request, 'pages/hair.html', context)

def exfoliate(request):
    all_products = Product.objects.filter(name='Southern Luxury Bar Soap')
    context = {'product': all_products}
    return render(request, 'pages/exfoliate.html', context)

def soap(request):
    all_products = Product.objects.filter(name='Rice Polish Exfoliant')
    context = {'product': all_products}
    return render(request, 'pages/soap.html')
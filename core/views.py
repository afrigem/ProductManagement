from django.shortcuts import render
from products.models import Category, Product

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, 'core/index.html',  {
        'categories': categories,
        'products': products,
    })

def contact (request):
    return render(request, 'core/contact.html',)


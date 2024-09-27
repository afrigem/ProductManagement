from django.shortcuts import render, get_object_or_404
from .models import Product

def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category).exclude(pk=pk)[0:3]

    return render(request, 'product/detail.html', {
        'product': product,
        'related_products': related_products
    })

from django.shortcuts import render
from products.models import Product
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    products = Product.objects.filter(created_by=request.user)
    
    return render(request, 'dashboard/index.html',{
        'products': products, 
    } )
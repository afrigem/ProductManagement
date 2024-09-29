from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import NewProductForm

def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(category=product.category).exclude(pk=pk)[0:3]

    return render(request, 'products/detail.html', {
        'product': product,
        'related_products': related_products
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)

        if form.is_valid():
            Product = form.save(commit=False)
            Product.created_by = request.user
            Product.save()

            return redirect('products:detail', pk=Product.id)
    else:   
        form = NewProductForm()

    return render(request, 'product/form.html', {
        'form': form,
        'title': 'New Product', 
    })
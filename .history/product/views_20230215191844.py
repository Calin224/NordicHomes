from django.shortcuts import render
from product.models import Product

# Create your views here.

def product(request, slug):
    product = get_object_or_404(slug=slug)
    
    context = {
        'product': product,
    }
    return render(request, 'product/product.html', context)
from django.shortcuts import render

# Create your views here.

def product(request, slug):
    return render(request, 'product/product.html')
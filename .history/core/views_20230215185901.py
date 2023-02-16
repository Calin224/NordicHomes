from django.shortcuts import render
from product.models import Category, Product

# Create your views here.

def frontpage(request):
    products = Product.objects.all()[0:8]
    context = {
        'products': products,
    }
    return render(request, 'core/frontpage.html', context)

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    
    active_category = reqyuest.GET.get('category')
    
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'core/shop.html', context)
from django.shortcuts import render, redirect
from product.models import Category, Product
from django.db.models import Q
from .forms import SignUpForm
from django.contrib.auth import login, authenticate

# Create your views here.

def frontpage(request):
    products = Product.objects.all()[0:8]
    context = {
        'products': products,
    }
    return render(request, 'core/frontpage.html', context)

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            return request('/')
        else:
            form=SignUpForm()
            
    context = {
        'form': form,
    }
    return render(request, 'core/signup.html', context)

def login_old(request):
    context = {}
    return render(request, 'core/login.html', context)


def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    
    active_category = request.GET.get('category', '')
    
    if active_category:
        products = products.filter(category__slug=active_category)
     
    query = request.GET.get('query', '') 
    
    if query:
        products = products.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query)
        )
    
    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category,
    }
    return render(request, 'core/shop.html', context)
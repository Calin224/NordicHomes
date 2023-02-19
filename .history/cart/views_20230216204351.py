from django.shortcuts import render
from .cart import Cart

# Create your views here.


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return render(request, 'cart/partials/menu_cart.html', {'cart': cart})

def cart(request):
    return render(request, 'cart/cart.html')

def checkout(request):
    return render(request, 'cart/checkout.html')
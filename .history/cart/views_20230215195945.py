from django.shortcuts import render,  get_object_or_404
from .cart import Cart

# Create your views here.


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return render(request, 'cart/partials/menu_cart.html', {'cart': cart})
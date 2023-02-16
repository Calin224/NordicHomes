from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .cart import Cart

# Create your views here.


def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect("cart:cart_detail")
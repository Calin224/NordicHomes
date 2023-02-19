from django.shortcuts import render, redirect
from .models import Order, OrderItem
from cart.cart import Cart


# Create your views here.

def start_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        place = request.POST['place']
        zipcode = request.POST['zipcode']

        order = Order.objects.create(user=request.user, first_name=first_name, last_name=last_name, email=email,
                                     phone=phone, address=address, place=place, zipcode=zipcode)

        for item in cart:
            product = item['product']
            quantity = int(item['quantity'])
            price = product.price * quantity

            item = OrderItem.objects.create(
                order=order, product=product, price=price, quantity=quantity)

        return redirect('myaccount')

    return redirect('cart')

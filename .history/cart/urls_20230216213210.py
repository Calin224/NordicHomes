from django.urls import path

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('cart/checkout', checkout, name='checkout'),
    path('add_to_cart/<int:product_id>', add_to_cart, name='add_to_cart'),
]
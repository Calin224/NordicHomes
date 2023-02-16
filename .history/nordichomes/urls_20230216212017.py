from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cart.views import add_to_cart,cart, checkout

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('cart/checkout', checkout, name='checkout'),
    path('add_to_cart/<int:product_id>', add_to_cart, name='add_to_cart'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path

from core.views import frontpage,shop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('shop/', shop, name='frontpage'),
]

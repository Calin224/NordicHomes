from django.conf import settings

from product.models import Product

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
            
        self.cart = cart    
        
    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)
            
    def __len__(self):
        return len(item['quantity'] for item in self.cart.values())
    
    def __save__(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
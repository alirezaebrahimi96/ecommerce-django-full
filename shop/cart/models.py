from django.db import models
from store.models import Product
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Cart(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return 'Cart #' + unicode(self.id)
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    def __unicode__(self):
        return 'Order #' + unicode(self.id) + ' of ' + self.product.title
from django.db import models
from store.models import Product
from django.conf import settings
User = settings.AUTH_USER_MODEL
import datetime

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
    
    
    
    
class Order(models.Model):
    products = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def get_order_by_customer(customer_id):
        return Order.objects.filter(customer=User)

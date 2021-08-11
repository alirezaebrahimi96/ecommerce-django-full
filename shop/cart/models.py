from django.db import models
from django.db.models.fields import NullBooleanField
from store.models import Product
from django.conf import settings
User = settings.AUTH_USER_MODEL
import datetime
from cupon.models import cupon


class CartItem(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    position = models.BooleanField(default=True)
    def __unicode__(self):
        return 'Order #' + unicode(self.id) + ' of ' + self.product.title

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

class Cart(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    def __unicode__(self):
        return 'Cart #' + unicode(self.user)
    def __str__(self):
        return str(self.updated_at) + ' for ' + str(self.user)
    
    


class Order(models.Model):
    cart = models.ManyToManyField(Cart)
    customer = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    status = models.BooleanField(default=False)
    off_code = models.CharField(max_length=15, null=True, blank=True)

    def get_order_by_customer(customer_id):
        return Order.objects.filter(customer=User)

    def __str__(self):
        return self.phone




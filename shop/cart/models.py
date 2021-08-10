from django.db import models
from django.db.models.fields import NullBooleanField
from store.models import Product
from django.conf import settings
User = settings.AUTH_USER_MODEL
import datetime



class CartItem(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return 'Order #' + unicode(self.id) + ' of ' + self.product.title
    def __str__(self):
        return str(self.user.username) + ': ' + str(self.product) + ' in ' + str(self.updated_at)
    
    

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
        return str(self.updated_at) + ' for ' + str(self.user.username) + ' with ' + str(self.user.phone)
    
    


class Order(models.Model):
    cart = models.ManyToManyField(Cart)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def get_order_by_customer(customer_id):
        return Order.objects.filter(customer=User)

    def __str__(self):
        return self.phone + 'in' + self.date
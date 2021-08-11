from django.shortcuts import render, HttpResponseRedirect, redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Cart, CartItem, Order
from store.models import Product
from django.views import View
from django.conf import settings
User = settings.AUTH_USER_MODEL
import datetime

##-------------- Cart Views --------------------------------------
class DetailCart(DetailView):
    model = Cart
    template_name='detail_cart.html'


class ListCart(ListView):
    model = Cart
    template_name = 'list_cart.html'


class CreateCart(CreateView):
    model = Cart
    fields = ['name', 'items']
    template_name = 'create_cart.html'

class UpdateCart(UpdateView):
    model = Cart
    fields = [
        "items",
    ]
    template_name = 'update_cart.html'

class DeleteCart(DeleteView):
    model = Cart
    template_name = 'delete_cart.html'


##-------------- CartItem Views --------------------------------------
class DetailCartItem(DetailView):
    model = CartItem
    template_name='detail_cartitem.html'

class ListCartItem(ListView):
    model = CartItem
    template_name='list_cartitem.html'

class CreateCartItem(CreateView):
    model = CartItem
    fields = ['product', 'quantity']    
    template_name = 'create_cartitem.html'
    

    
class UpdateCartItem(UpdateView):
    model = CartItem
    cartitem = CartItem.objects.all()
    for item in cartitem:
        item.position = True
        item.save()
    fields = ['product', 'quantity']
    template_name = 'update_cartitem.html'
   
    
class DeleteCartItem(DeleteView):
    model = CartItem    
    template_name = 'delete_cartitem.html'
    
class DetailOrder(DetailView):
    model = Order
    template_name='detail_order.html'

class ListOrder(ListView):
    model = Order
    context_object_name = 'orders'
    template_name='list_order.html'
    
    
class CreateOrder(CreateView):
    model = Order
    fields = ['cart', 'address', 'phone', 'off_code']
    template_name = 'create_order.html'
    
    
class UpdateOrder(UpdateView):
    model = Order
    fields = ['cart', 'address', 'phone', 'off_code']
    template_name = 'update_cart.html'

class DeleteOrder(DeleteView):
    model = Order
    template_name = 'delete_cart.html'
    


    
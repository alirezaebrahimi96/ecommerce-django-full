
from django.urls import path

from cart import views

app_name = 'cart'   

urlpatterns = [
    path('get_cart_count/', views.get_cart_count, name='get_cart_count'),
    path("get_user_cart/", views.get_user_cart, name="get_user_cart"),
    path("update_cart_info/", views.update_cart_info, name="update_cart_info"),
    path("view_cart/", views.view_cart, name="view_cart"),
    path("add_to_cart/<slug>/", views.add_to_cart, name="add_to_cart"),
    path("remove_from_cart/<id>", views.remove_from_cart, name="remove_from_cart"),
]
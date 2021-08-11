from django.urls import path, include

from . import views

# Cart Urls
urlpatterns = [
    path('cart/', views.ListCart.as_view(), name='list-carts'),
    path('cart/<int:pk>/', views.DetailCart.as_view(), name='detail-cart'),
    path('cart/create/', views.CreateCart.as_view(), name='create-cart'),
    path('cart/<int:pk>/update/', views.UpdateCart.as_view(), name='update-cart'),
    path('cart/<int:pk>/delete/', views.DeleteCart.as_view(), name='delete-cart'),
]

# CartItem Urls
urlpatterns += [
    path('cartitem/', views.ListCartItem.as_view(), name='list-cartitem'),
    path('cartitem/<int:pk>/', views.DetailCartItem.as_view(), name='detail-cartitem'),
    path('cartitem/create/', views.CreateCartItem.as_view(), name='create-cartitem'),
    path('cartitem/<int:pk>/update/', views.UpdateCartItem.as_view(), name='update-cartitem'),
    path('cartitem/<int:pk>/delete/', views.DeleteCartItem.as_view(success_url="/cartitem/"), name='delete-cartitem'),
]

urlpatterns += [
    path('order/', views.ListOrder.as_view(), name='list-order'),
    path('order/<int:pk>/', views.DetailOrder.as_view(), name='detail-order'),
    path('order/create/', views.CreateOrder.as_view(), name='create-order'),
    path('order/<int:pk>/update/', views.UpdateOrder.as_view(), name='update-order'),
    path('order/<int:pk>/delete/', views.DeleteOrder.as_view(), name='delete-order'),
]


from django.urls import path

from store import views

app_name = 'store'   

urlpatterns = [
    #path('', views.homepage, name='homepage'),
    path("register/", views.register_request, name="register"),

]

from django.urls import path

from store import views

app_name = 'store'   

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("news/", views.news, name="news"),
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),

]
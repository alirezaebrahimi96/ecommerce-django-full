from json import JSONEncoder
from datetime import datetime
import random
from django.core import serializers
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models import Sum, Count
from django.http import JsonResponse
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.http import require_POST
import string
from .utils import RateLimited
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

random_str = lambda N: ''.join(
    random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(N))


from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from . import models
from .serializers import UserSerializer, AuthTokenSerializer

class CreateUserView(generics.CreateAPIView):
    
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES    
    
    
def homepage(request):
    products = models.Product.objects.all()
    products_serialized = serializers.serialize('json', products)
    categories = models.Category.objects.all()
    categories_serialized = serializers.serialize('json', categories)
    return JsonResponse(products_serialized, encoder=JSONEncoder, safe=False)


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


@csrf_exempt
@require_POST
def login_request(request):
    if request.method == "POST":
	    form = AuthenticationForm(request, data=request.POST)
	    if form.is_valid():
		    username = form.cleaned_data.get('username')
		    password = form.cleaned_data.get('password')
		    user = authenticate(username=username, password=password)
		    if user is not None:
			    login(request, user)
			    messages.info(request, f"You are now logged in as {username}.")
			    return redirect("store:homepage")
		    else:
			    messages.error(request,"Invalid username or password.")
	    else:
		    messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return JsonResponse(context={"login_form":form}, encoder=JSONEncoder)




@csrf_exempt
def news(request):
    news = models.News.objects.all().order_by('-date')[:11]
    news_serialized = serializers.serialize("json", news)
    return JsonResponse(news_serialized, encoder=JSONEncoder, safe=False)


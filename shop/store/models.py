from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
import datetime
from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class MyUserManager(BaseUserManager):
    def _create_user(self, first_name, last_name, phone, address1, state, zipcode, email, username, password, is_superuser):

        user=self.model(
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            address1 = address1,
            zipcode = zipcode,
            state = state,
            email=email, 
            username = username,
            password = password,
            is_superuser = is_superuser,
            )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, first_name, last_name, phone, address1, state, zipcode, email, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(first_name, last_name, phone, address1, state, zipcode, email, username, password, **extra_fields)

    def create_superuser(self, first_name, last_name, phone, address1, state, zipcode, email, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)  
                                 
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(first_name, last_name, phone, address1, state, zipcode, email, username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.DecimalField(max_digits=12, decimal_places=0, unique=True)
    address1 = models.CharField(null=True, max_length=100, blank=True)
    zipcode = models.CharField(max_length=10, null=True,blank=True)
    state = models.CharField(null=True, max_length=25, blank=True)
    email = models.EmailField(max_length = 250, unique=True)
    username = models.CharField(max_length = 25, unique=True)
    password = models.CharField(max_length =25, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    
    objects = MyUserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'phone', 'password', 'zipcode', 'address1', 'state']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return f'{self.first_name} ({self.last_name}) ({self.email})'





choices = (
    ('preffer', 'preffer'),
    ('too bad', 'too bad'),
    ("I don't know", "I don't know")
)

class Picture(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products/images", blank=True)

class Comment(models.Model):
    author = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    star = models.DecimalField(max_digits=1, decimal_places=0)
    sense = models.CharField(max_length=50, choices=choices, default='like')


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self',
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store:category", kwargs={"name": self.name})



class Product(models.Model):
    #author = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500, default="Empty description.")    
    category = models.ManyToManyField(Category, blank=True)
    comment = models.ManyToManyField(Comment, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    tags = TaggableManager(blank=True)
    picture = models.ManyToManyField(Picture, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    quantity = models.PositiveIntegerField(default=10)
    quantity_in_store = models.PositiveIntegerField()
    featured = models.BooleanField(default=False)     
    
    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    @property
    def is_featured(self):
        return self.featured

    @property
    def is_available(self):
        return self.quantity > 0
    
    
    
class News(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(blank = True)
    date = models.DateTimeField(auto_now_add=True)
    picture = models.ManyToManyField(Picture, blank=True)
    
    def __unicode__(self):
        return self.title
    

    
class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(blank = True)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.ManyToManyField(Comment, blank=True)
    picture = models.ManyToManyField(Picture, blank=True)


    def __unicode__(self):
        return self.title
    
    

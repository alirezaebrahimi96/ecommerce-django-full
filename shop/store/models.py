from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
                              
                              
                                        
class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user 
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'



choices = (
    ('preffer', 'preffer'),
    ('too bad', 'too bad'),
    ("I don't know", "I don't know")
)



class Comment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500, default="Empty description.")    
    category = models.ManyToManyField(Category, blank=True)
    comment = models.ManyToManyField(Comment, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    tags = TaggableManager(blank=True)
    picture = models.ImageField(upload_to="products/images", null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    quantity = models.IntegerField(default=10)
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
    
    
    
    
class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)

    def __unicode__(self):
        return "{}_token".format(self.user)
    
    
    
    
class News(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(blank = True)
    date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title
    

    

class Passwordresetcodes(models.Model):
    code = models.CharField(max_length=32)
    email = models.CharField(max_length=120)
    time = models.DateTimeField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    
    
class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(blank = True)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.ManyToManyField(Comment, blank=True)

    def __unicode__(self):
        return self.title
    
    

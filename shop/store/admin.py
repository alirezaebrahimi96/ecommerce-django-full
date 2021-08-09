from django.contrib import admin
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import Category, Product, Comment, News, Post, MyUserManager, CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from store import models
from . import forms
from cart.models import Cart, CartItem
# Register your models here.

        
class MyUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = forms.NewUserForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ("first_name","last_name","address1","zipcode","state", "username", "email",'phone', "password",'is_staff')
    list_filter = ('username',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username')}),
        ('Personal info', {'fields': ('address1', 'zipcode', 'state', 'first_name', 'last_name', 'phone')}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'password'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(CustomUser, MyUserAdmin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(News)

admin.site.register(Cart)
admin.site.register(CartItem)
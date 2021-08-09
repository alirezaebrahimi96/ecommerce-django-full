from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser


# Create your forms here.

class NewUserForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    address1 = forms.CharField(required=True)
    zipcode = forms.CharField(required=True)
    state = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.DecimalField(max_digits=12, decimal_places=0, required=True)
    class Meta:
	    model = CustomUser
	    fields = ("first_name","last_name","address1","zipcode","state", "username", "email",'phone')

    def save(self, commit=True):
	    user = super(NewUserForm, self).save(commit=False)
	    user.email = self.cleaned_data['email']
	    user.phone = self.cleaned_data['phone']
	    if commit:
		    user.save()
	    return user
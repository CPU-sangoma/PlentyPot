from django import forms
from django.forms import ModelForm
from .models import BusinessProfile, CustomerProfile


class BusinessProForm(forms.ModelForm):
    class Meta:
        model = BusinessProfile
        exclude = ('longitude','latitude','Complete','recommendations','user')


class CustomerProForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        exclude = ('user',)

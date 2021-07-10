from django import forms
from django.forms import ModelForm
from .models import SalonHomeModel,SalonPricesModel



class SalonHomeForm(forms.ModelForm):

    class Meta:
        model=SalonHomeModel
        exclude= ('company','status',)


class SalonPricesForm(forms.ModelForm):

    class Meta:
        model=SalonPricesModel
        exclude = ('company','status',)

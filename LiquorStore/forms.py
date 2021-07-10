from django import forms
from django.forms import ModelForm
from .models import LiquorHomePageModel, LiquorSalesModel




class LiquorHomeForm(forms.ModelForm):
    
    class Meta:
        model = LiquorHomePageModel
        exclude = ('company','status',)

class LiquorSaleForm(forms.ModelForm):
    
    class Meta:
        model = LiquorSalesModel
        exclude = ('company','status',)
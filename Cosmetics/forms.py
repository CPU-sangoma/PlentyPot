from django import forms
from django.forms import ModelForm
from .models import CosmeticsHomePage,CosmeticsWork



class CosmeticsHomeForm(forms.ModelForm):
    
    class Meta:
        model = CosmeticsHomePage
        exclude = ("company",'status',)
        
        
        
class CosmeticsWorkForm(forms.ModelForm):
    
    class Meta:
        model = CosmeticsWork
        exclude = ("company",'status',)

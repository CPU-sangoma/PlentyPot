
from django import forms
from django.forms import ModelForm
from .models import Reviews

class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Reviews
        exclude = ('author','reviewing','time','date',)
from django import forms
from .models import CusUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

class CusUserCreation(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CusUser
        fields = UserCreationForm.Meta.fields + ('Account','last_name','first_name','email')


class CusUserChange(UserChangeForm):
    class Meta:
        model = CusUser
        fields = UserChangeForm.Meta.fields
        


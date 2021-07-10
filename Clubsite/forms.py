from django import forms
from django.forms import ModelForm
from Clubsite.models import EventsPageModel,HomePageModel,TonightModel



class TonightForm(forms.ModelForm):
    
    class Meta:
        model = TonightModel
        exclude = ("company","status",)
        
        
class EventsForm(forms.ModelForm):
    
    class Meta:
        model = EventsPageModel
        exclude = ("company","status")
                  
class HomeForm(forms.ModelForm):
    
    class Meta:
        model = HomePageModel
        exclude = ("company","status")
                  

        

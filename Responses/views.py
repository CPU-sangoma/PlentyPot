from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Reviews
from profiles.models import BusinessProfile
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required
def ReviewsView(request,business):
    company = BusinessProfile.objects.filter(id=business).first()
    if request.method == "POST":
        form = ReviewForm(request.POST,request.FILES)
        if form.is_valid():
            rv = Reviews()
            rv.author = request.user
            rv.reviewing = company
            rv.picture = form.cleaned_data['picture']
            rv.body = form.cleaned_data['body']
            rv.save()
            messages.success(request,'review posted')
            return redirect('reviews',business=business)
            
            
    else:
        form = ReviewForm()
    
    reviews = Reviews.objects.filter(reviewing_id=business)
        
    return render(request,'inside/reviews.html',{'form':form,'reviews':reviews})


def NearMapView(request,tob):
    business = BusinessProfile.objects.filter(type_of_business=tob)
    return render(request,'inside/nearbymap.html',{'businesses':business,'tob':tob})
    
    
    
    
   

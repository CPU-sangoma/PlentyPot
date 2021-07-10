from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from profiles.models import BusinessProfile
from .models import Recommend
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def RecommendView(request):
    
    busId = request.POST['Recname']
    recommendAvail = Recommend.objects.filter(Recommend_by=request.user).filter(Recommended_company=busId).count()
    
    if recommendAvail <= 0:
        recUser = request.user
        recBusiness = BusinessProfile.objects.filter(id=busId).first()
        Rec = Recommend()
        Rec.Recommend_by = recUser
        Rec.Recommended_company = recBusiness
        Rec.save()
    
        count = Recommend.objects.filter(Recommended_company_id=busId).count()
        bus = BusinessProfile.objects.get(id=busId)
        bus.recommendations = count
        bus.save()
        
        messages.success(request,'you recommend this business')
        return redirect('details', tob=bus.type_of_business, id=busId)
    else:
        
        
        recRow = Recommend.objects.filter(Recommend_by=request.user).filter(Recommended_company=busId)
        recRow.delete()
        
        
        count = Recommend.objects.filter(Recommended_company_id=busId).count()
        bus = BusinessProfile.objects.get(id=busId)
        bus.recommendations = count
        bus.save()
        messages.warning(request,'you no longer recommend this business')
        return redirect('details', tob=bus.type_of_business, id=busId)
      
        
        
        
        
    


    
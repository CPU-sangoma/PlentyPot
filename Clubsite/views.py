from django.shortcuts import render,redirect
from .forms import EventsForm,TonightForm,HomeForm
from .models import HomePageModel,EventsPageModel,TonightModel
from django.contrib import messages
from django.http import HttpResponseRedirect
from profiles.models import BusinessProfile
# Create your views here.

def ClubHomepage(request,name):
    bus = BusinessProfile.objects.get(business_name=name)
    homepage = HomePageModel.objects.get(company_id=bus.id)
    if homepage.PageComplete ==1:

        if homepage.status == 1:
            return render(request,'websites/Club/Home.html',{"homedata":homepage,"business":bus})
        else:
            messages.success(request,"unfortunately that website is suspended or does not exist, try visiting another")
            return redirect('home')
    else:
        messages.warning(request,"The owner is not yet done editing their website")
        return redirect('details',tob=bus.type_of_business, id=bus.id)



def ClubTonightpage(request,name):

    bus = BusinessProfile.objects.get(business_name=name)
    Tonightpage = TonightModel.objects.get(company_id=bus.id)

    if Tonightpage.PageComplete == 1:

        if Tonightpage.status == 1:
            return render(request,'websites/Club/Tonight.html',{"tonightdata":Tonightpage,"business":bus})
        else:
            messages.success(request,"unfortunately that website is suspended or does not exist, try visiting another")
            return redirect('home')
    else:
        messages.warning(request,"The owner is not yet done editing their website")
        return redirect('details',tob=bus.type_of_business, id=bus.id)


def ClubEventspage(request,name):
    bus = BusinessProfile.objects.get(business_name=name)
    eventspage = EventsPageModel.objects.get(company_id=bus.id)

    if eventspage.PageComplete == 1:

        if eventspage.status == 1:
            return render(request,'websites/Club/Events.html',{'eventsdata':eventspage,'business':bus})
        else:
            messages.success(request,"unfortunately that website is suspended or does not exist, try visiting another")
            return redirect('home')
    else:
        messages.warning(request,"The owner is not yet done editing their website")
        return redirect('details',tob=bus.type_of_business, id=bus.id)


def ClubContacts(request,name):
    bus = BusinessProfile.objects.get(business_name=name)
    contact = TonightModel.objects.get(company_id=bus.id)
    return render(request,"websites/Club/Contact.html",{'contactdata':contact,'business':bus})



def EditClubHome(request):


    test = HomePageModel.objects.get(company_id=request.user.businesspro.id)

    if test.status == 1:
        if request.method == "POST":
            form = HomeForm(request.POST,request.FILES,instance=request.user.businesspro.clubhome)

            if form.is_valid():
                form.save()
                test.PageComplete = 1
                test.save()
                messages.success(request, 'Homepage successfully updated')
                return HttpResponseRedirect(request.path_info)

        else:
            form = HomeForm(instance=request.user.businesspro.clubhome)

        return render(request,'websites/Club/Edithome.html',{'form':form})
    else:
        messages.warning(request,"seems your account is suspended or not activated, please pay the required fees")
        return redirect('home')

def EditClubTonight(request):

    test = TonightModel.objects.get(company_id=request.user.businesspro.id)

    if request.method == "POST":
        form = TonightForm(request.POST,request.FILES,instance=request.user.businesspro.clubTonight)

        if form.is_valid():
            form.save()
            test.PageComplete = 1
            test.save()
            messages.success(request, 'Tonightpage successfully updated')
            return HttpResponseRedirect(request.path_info)

    else:
        form = TonightForm(instance=request.user.businesspro.clubTonight)

    return render(request,'websites/Club/Edithome.html',{'form':form})

def EditClubEvents(request):
    test = EventsPageModel.objects.get(company_id=request.user.businesspro.id)

    if request.method == "POST":
        form = EventsForm(request.POST,request.FILES,instance=request.user.businesspro.clubEvents)

        if form.is_valid():
            form.save()
            test.PageComplete = 1
            test.save()
            messages.success(request, 'Eventspage successfully updated')
            return HttpResponseRedirect(request.path_info)

    else:
        form = EventsForm(instance=request.user.businesspro.clubEvents)

    return render(request,'websites/Club/Edithome.html',{'form':form})



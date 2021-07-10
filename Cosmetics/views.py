from django.shortcuts import render,redirect
from .models import CosmeticsHomePage, CosmeticsWork, ActualCosWork
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import CosmeticsHomeForm,CosmeticsWorkForm
from profiles.models import BusinessProfile
# Create your views here.


def CosmeticsHomePageView(request,name):
    bus = BusinessProfile.objects.get(business_name=name)
    homepage = CosmeticsHomePage.objects.get(company_id=bus.id)
    if homepage.PageComplete == 1:

        if homepage.status == 1:
            return render(request,'websites/Cosmetics/site/Homepage.html',{'homedata':homepage,'business':bus})
        else:
            messages.success(request,"unfortunately that website is suspended or does not exist, try visiting another")
            return redirect('home')
    else:
        messages.warning(request,"The owner is not yet done editing their website")
        return redirect('details',tob=bus.type_of_business, id=bus.id)


def CosmeticsWorkPage(request,name):
    bus = BusinessProfile.objects.get(business_name=name)
    work = CosmeticsWork.objects.get(company_id=bus.id)
    actwork = ActualCosWork.objects.filter(company_id=bus.id)

    if work.PageComplete == 1:

        if work.status == 1:
            return render(request,"websites/Cosmetics/site/Workpage.html",{'workdata':actwork,'business':bus})
        else:
            messages.success(request,"unfortunately that website is suspended or does not exist, try visiting another")
            return redirect('home')
    else:
        messages.warning(request,"The owner is not yet done editing their website")
        return redirect('details',tob=bus.type_of_business, id=bus.id)


def CosmeticsContactPage(request,name):

    bus = BusinessProfile.objects.get(business_name=name)
    return render(request,'websites/Cosmetics/site/Contactpage.html',{'business':bus})






def EditCosmeticsHome(request):

    test = CosmeticsHomePage.objects.get(company_id=request.user.businesspro.id)

    if test.status == 1:

        if request.method == "POST":
            form = CosmeticsHomeForm(request.POST,request.FILES,instance=request.user.businesspro.cosmeticshome)

            if form.is_valid():
                test.PageComplete = 1
                test.save()
                form.save()
                messages.success(request, 'Homepage successfully updated')
                return HttpResponseRedirect(request.path_info)

        else:
            form = CosmeticsHomeForm(instance=request.user.businesspro.cosmeticshome)

        return render(request,'websites/Cosmetics/Edithome.html',{'form':form})
    else:
        messages.warning(request,"seems your account is suspended or not activated, please pay the required fees")
        return redirect('home')

def EditCosmeticsWork(request):
    test = CosmeticsWork.objects.get(company_id=request.user.businesspro.id)
    actualCos = ActualCosWork()
    infos = ActualCosWork.objects.filter(company_id = request.user.businesspro.id)

    if request.method == "POST":

        test.PageComplete = 1
        test.save()
        actualCos.company = request.user.businesspro
        actualCos.Workdes = request.POST['cosdes']
        actualCos.Workpic = request.FILES['cospic']
        actualCos.save()
        messages.success(request, 'Work page successfully updated')

        return HttpResponseRedirect(request.path_info)

    else:
        pass

    return render(request,'websites/Cosmetics/Editwork.html',{'infos':infos})

def DeleteWork(request):
    actual = ActualCosWork.objects.filter(id = request.POST['workid'])
    actual.delete()
    messages.success(request,'picture successfully deleted')
    return redirect('cosmeticseditwork')

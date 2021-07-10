from django.shortcuts import render,redirect
from django.contrib import messages
from .models import BusinessProfile,SalonHomeModel,SalonPricesModel, ActualSalonModel
from .forms import SalonHomeForm,SalonPricesForm
from django.http import HttpResponseRedirect


# Create your views here.




def EditSalonHome(request):

    test = SalonHomeModel.objects.get(company_id=request.user.businesspro.id)

    if test.status == 1:

        if request.method == "POST":
            form = SalonHomeForm(request.POST,request.FILES,instance=request.user.businesspro.salonhome)

            if form.is_valid():
                test.PageComplete = 1
                test.save()
                form.save()

                messages.success(request, 'Homepage successfully updated')
                return HttpResponseRedirect(request.path_info)

        else:
            form = SalonHomeForm(instance=request.user.businesspro.salonhome)

        return render(request,'websites/Salon/edit/Editsalonhome.html',{'form':form})
    else:
        messages.warning(request,"seems your account is suspended or not activated, please pay the required fees")
        return redirect('home')

def EditSalonPrices(request):

    test = SalonPricesModel.objects.get(company_id=request.user.businesspro.id)
    actual = ActualSalonModel()
    infos = ActualSalonModel.objects.filter(company_id=request.user.businesspro.id)


    if request.method == "POST":

        test.PageComplete = 1
        test.save()
        actual.company = request.user.businesspro
        actual.styledes = request.POST['styledes']
        actual.stylepic = request.FILES['stylepic']
        actual.save()
        messages.success(request, 'styles page successfully updated')
        return HttpResponseRedirect(request.path_info)

    else:
        pass

    return render(request,'websites/Salon/edit/Editsalonprices.html',{'infos':infos})



def SalonHomepage(request,name):
    bus = BusinessProfile.objects.get(business_name=name)
    homepage = SalonHomeModel.objects.get(company_id=bus.id)

    if homepage.PageComplete == 1:
        if homepage.status == 1:
            return render(request,'websites/Salon/site/salonhome.html',{"homedata":homepage,"business":bus})
        else:
            messages.warning(request,"unfortunately that website is suspended or does not exist, try visiting another")
            return redirect('home')
    else:
        messages.warning(request,"The owner is not yet done editing their website")
        return redirect('details',tob=bus.type_of_business, id=bus.id)







def SalonPricespage(request,name):
    bus = BusinessProfile.objects.get(business_name=name)
    pricepage = SalonPricesModel.objects.get(company_id=bus.id)
    actualprice = ActualSalonModel.objects.filter(company_id=bus.id)

    if pricepage.PageComplete == 1:
        if pricepage.status == 1:
            return render(request,'websites/Salon/site/salonprices.html',{"pricedata":actualprice,"business":bus})
        else:
            messages.success(request,"unfortunately that website is suspended or does not exist, try visiting another")
            return redirect('home')
    else:
        messages.warning(request,"The owner is not yet done editing their website")
        return redirect('details',tob=bus.type_of_business, id=bus.id)


def Saloncontacts(request,name):
    bus = BusinessProfile.objects.get(business_name=name)
    pricepage = SalonHomeModel.objects.get(company_id=bus.id)

    if pricepage.PageComplete == 1 :
        if pricepage.status == 1:
            return render(request,'websites/Salon/site/saloncontact.html',{"business":bus})
    else:
        messages.warning(request,"The owner is not yet done editing their website")
        return redirect('details',tob=bus.type_of_business, id=bus.id)

def DeleteStyle(request):

    actual = ActualSalonModel.objects.filter(id=request.POST['styleid'])
    actual.delete()
    messages.success(request,'style successfully deleted from page')
    return redirect('editsalonprices')

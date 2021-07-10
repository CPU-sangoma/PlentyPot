from django.shortcuts import render,redirect
from .forms import LiquorHomeForm,LiquorSaleForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from profiles.models import BusinessProfile
from .models import LiquorHomePageModel,LiquorSalesModel,ActualLiqSales

# Create your views here.


def EditLiquorHome(request):

    test = LiquorHomePageModel.objects.get(company_id=request.user.businesspro.id)

    if test.status == 1:

        if request.method == "POST":
            form = LiquorHomeForm(request.POST,request.FILES,instance=request.user.businesspro.liquorhome)

            if form.is_valid():
                test.PageComplete = 1
                test.save()
                form.save()

                messages.success(request, 'Homepage successfully updated')
                return HttpResponseRedirect(request.path_info)

        else:
            form = LiquorHomeForm(instance=request.user.businesspro.liquorhome)

        return render(request,'websites/LiquorStore/Editliquorhome.html',{'form':form})
    else:
        messages.warning(request,"seems your account is suspended or not activated, please pay the required fees")
        return redirect('home')

def EditLiquorSales(request):
    test = LiquorSalesModel.objects.get(company_id=request.user.businesspro.id)
    actualsal = ActualLiqSales()
    infos = ActualLiqSales.objects.filter(company_id=request.user.businesspro.id)
    if request.method == "POST":
            test.PageComplete = 1
            actualsal.company = request.user.businesspro
            actualsal.salepic = request.FILES['salepic']
            actualsal.saledes = request.POST['saledes']
            actualsal.save()
            test.save()
            messages.success(request, 'salespage successfully updated')
            return HttpResponseRedirect(request.path_info)

    else:
        pass

    return render(request,'websites/LiquorStore/Editliquorsales.html',{'infos':infos})

def DeleteSaleItem(request):
    info = ActualLiqSales.objects.filter(company_id=request.user.businesspro.id)

    actual = ActualLiqSales.objects.filter(id=request.POST['Liqsale'])
    actual.delete()
    messages.success(request,'item deleted successfuly')
    return redirect('editliquorsales')




def LiquorHomepage(request,name):
    bus = BusinessProfile.objects.get(business_name=name)
    homepage = LiquorHomePageModel.objects.get(company_id=bus.id)

    if homepage.PageComplete == 1:

        if homepage.status == 1:
            return render(request,'websites/LiquorStore/Liquorhome.html',{"homedata":homepage,"business":bus})
        else:
            messages.warning(request,"unfortunately that website is suspended or does not exist, try visiting another")
            return redirect('home')
    else:
        messages.warning(request,"The owner is not yet done editing their website")
        return redirect('details',tob=bus.type_of_business, id=bus.id)


def LiquorSalespage(request,name):

    bus = BusinessProfile.objects.get(business_name=name)
    Sales = LiquorSalesModel.objects.get(company_id=bus.id)

    if Sales.PageComplete == 1:

        if Sales.status == 1:
            return render(request,'websites/LiquorStore/Liquorsales.html',{"sales":Sales,"business":bus})
        else:
            messages.warning(request,"unfortunately that website is suspended or does not exist, try visiting another")
            return redirect('home')
    else:
        messages.warning(request,"The owner is not yet done editing their website")
        return redirect('details',tob=bus.type_of_business, id=bus.id)


def LiquorContacts(request,name):
    bus = BusinessProfile.objects.get(business_name=name)
    return render(request,"websites/LiquorStore/liquorcontacts.html",{'business':bus})



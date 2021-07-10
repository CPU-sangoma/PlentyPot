from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import FoodHomeForm,FoodMenuForm
from django.contrib import messages
from profiles.models import BusinessProfile
from FoodStore.models import FoodHomePageModel,FullMenuPageModel, ActualMenuModel

# Create your views here.




def FoodHomePage(request,name):


    bus = BusinessProfile.objects.get(business_name=name)
    homepage = FoodHomePageModel.objects.get(company_id=bus.id)

    if homepage .PageComplete == 1:

        if homepage.status == 1:
            return render(request,'websites/Food/site/Foodhomepage.html',{'homedata':homepage,'business':bus})
        else:
            messages.success(request,"unfortunately that website is suspended or does not exist, try visiting another")
            return redirect('home')
    else:
        messages.warning(request,"The owner is not yet done editing their website")
        return redirect('details',tob=bus.type_of_business, id=bus.id)


def FoodMenu(request,name):
    bus = BusinessProfile.objects.get(business_name=name)
    menu = FullMenuPageModel.objects.get(company_id=bus.id)
    acmenu = ActualMenuModel.objects.filter(company_id=bus.id)

    if menu.PageComplete == 1:

        if menu.status == 1:
            return render(request,"websites/Food/site/Foodmenupage.html",{'menudata':acmenu,'business':bus})
        else:
            messages.warning(request,"unfortunately that website is suspended or does not exist, try visiting another")
            return redirect('home')

    else:
        messages.warning(request,"The owner is not yet done editing their website")
        return redirect('details',tob=bus.type_of_business, id=bus.id)


def FoodContactPage(request,name):
    bus = BusinessProfile.objects.get(business_name=name)
    return render(request,'websites/Food/site/Foodcontactpage.html',{'business':bus})







def EditFoodHome(request):

    test = FoodHomePageModel.objects.get(company_id=request.user.businesspro.id)

    if test.status == 1:
        if request.method == "POST":
            form = FoodHomeForm(request.POST,request.FILES,instance=request.user.businesspro.foodhome)

            if form.is_valid():
                test.PageComplete = 1
                form.save()
                test.save()
                messages.success(request, 'Homepage successfully updated')
                return HttpResponseRedirect(request.path_info)

        else:
            form = FoodHomeForm(instance=request.user.businesspro.foodhome)

        return render(request,'websites/Food/Edit/FoodHome.html',{'form':form})
    else:
        messages.warning(request,"seems your account is suspended or not activated, please pay the required fees")
        return redirect('home')

def EditFoodMenu(request):
    test = FullMenuPageModel.objects.get(company_id=request.user.businesspro.id)
    actual = ActualMenuModel()
    info = ActualMenuModel.objects.filter(company_id=request.user.businesspro.id)
    if request.method == "POST":

        test.PageComplete = 1
        actual.company = request.user.businesspro
        actual.menudes = request.POST['des']
        actual.menupic =  request.FILES['slotpic']
        actual.save()
        test.save()


        messages.success(request,'item added to menu')
        return HttpResponseRedirect(request.path_info)

    else:
        return render(request,'websites/Food/Edit/Foodmenu.html',{'infos':info})



    return render(request,'websites/Food/Edit/Foodmenu.html',{'infos':info})

def DeleteMenuItem(request):
    info = ActualMenuModel.objects.filter(company_id=request.user.businesspro.id)

    actual = ActualMenuModel.objects.filter(id=request.POST['food'])
    actual.delete()
    messages.success(request,'item deleted successfuly')
    return redirect('Editfoodmenu')







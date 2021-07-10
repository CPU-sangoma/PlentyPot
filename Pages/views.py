from django.shortcuts import render, redirect
from Users.forms import CusUserCreation
from profiles.forms import BusinessProForm, CustomerProForm, BusinessProfile, CustomerProfile
from Users.models import CusUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from Recommend.models import Recommend
from Clubsite.models import EventsPageModel,HomePageModel,TonightModel
from Clubsite.forms import HomeForm,EventsForm,TonightForm
from LiquorStore.models import LiquorHomePageModel, LiquorSalesModel
from Cosmetics.models import CosmeticsHomePage,CosmeticsWork
from FoodStore.models import FoodHomePageModel,FullMenuPageModel
from Salon.models import SalonHomeModel,SalonPricesModel

# Create your views here.
def HomeView(request):
    username = request.user.username
    CurrentUser = CusUser.objects.filter(username=username).first()
    return render(request, 'inside/home.html', {'currentuser': CurrentUser})

@login_required
def BusinessProfilesView(request):
    return render(request, 'inside/My_businessprofile.html')

@login_required
def CustomerProfilesView(request):
    return render(request, 'inside/My_customerprofile.html')


def signupView(request):
    if request.method == "POST":
        form = CusUserCreation(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully signed up, you may login')
            return redirect('login')
    else:
        form = CusUserCreation()
    return render(request, 'Registration/signup.html', {'form': form})

@login_required
def EditProfileView(request):

    pro= BusinessProfile.objects.get(user_id=request.user.id)
    if request.user.Account == "Business":
        if request.method == "POST":
            form = BusinessProForm(request.POST,request.FILES,instance=request.user.businesspro)
            if form.is_valid():
                form.instance.latitude = float(request.POST['lat'])
                form.instance.longitude = float(request.POST['long'])



                if pro.Complete == 0:

                    if request.user.businesspro.type_of_business == "Club":
                        homepage = HomePageModel()
                        homepage.company_id = request.user.businesspro.id
                        homepage.save()

                        eventpage = EventsPageModel()
                        eventpage.company_id = request.user.businesspro.id
                        eventpage.save()

                        tonight = TonightModel()
                        tonight.company_id = request.user.businesspro.id
                        tonight.save()

                    elif request.user.businesspro.type_of_business == "LiquorStore":

                        Liquorhome = LiquorHomePageModel()
                        Liquorhome.company_id = request.user.businesspro.id
                        Liquorhome.save()

                        sales = LiquorSalesModel()
                        sales.company_id = request.user.businesspro.id
                        sales.save()

                    elif request.user.businesspro.type_of_business == "Cosmetics":

                        coshome = CosmeticsHomePage()
                        coshome.company_id = request.user.businesspro.id
                        coshome.save()

                        coswork = CosmeticsWork()
                        coswork.company_id = request.user.businesspro.id
                        coswork.save()

                    elif request.user.businesspro.type_of_business == "Food":

                        foodhome = FoodHomePageModel()
                        foodhome.company_id = request.user.businesspro.id
                        foodhome.save()

                        foodmenu = FullMenuPageModel()
                        foodmenu.company_id = request.user.businesspro.id
                        foodmenu.save()

                    elif request.user.businesspro.type_of_business == "Salon":

                        salonhome = SalonHomeModel()
                        salonhome.company_id = request.user.businesspro.id
                        salonhome.save()

                        salonprices = SalonPricesModel()
                        salonprices.company_id = request.user.businesspro.id
                        salonprices.save()


                else:
                    pass


                form.instance.Complete = 1
                form.save()


                messages.success(request, 'profile successfully updated')
                return redirect('BusinessPro')
            else:
                messages.warning(request, 'profile not updated')
                return redirect('BusinessPro')
        else:
            form = BusinessProForm(instance=request.user.businesspro)
    else:
        if request.method == "POST":
            form = CustomerProForm(request.POST,request.FILES,instance=request.user.customerpro)
            if form.is_valid():
              form.save()
              messages.success(request, 'profile successfully updated')
              return redirect('CustomerPro')
            else:
                messages.warning(request, 'profile not updated')
                return redirect('CustomerPro')
        else:
            form = CustomerProForm(instance=request.user.customerpro)




    return render(request, 'inside/editprofile.html', {'form': form,'pro':pro})

def CategoryMenu(request,cat):
    business_list = BusinessProfile.objects.filter(type_of_business = cat).order_by('-recommendations')
    business = Paginator(business_list,2)

    page = request.GET.get('page')
    businesses =business.get_page(page)

    return render(request,'inside/categoryMenu.html',{'type':cat,'businesses':businesses})

def SearchedView(request):

    location = request.GET['Location']
    bustype = request.GET['type']
    locationlist = location.split()
    province = locationlist[0]
    city = locationlist[-1]

    businesses = BusinessProfile.objects.filter(province=province).filter(city=city).filter(type_of_business=bustype).order_by('-recommendations')

    return render(request,'inside/searchedmenu.html',{'businesses':businesses})


def DetailPageView(request,tob,id):

    business = BusinessProfile.objects.filter(type_of_business=tob).filter(id=id).first()

    return render(request,'inside/detailspage.html',{'business':business})


def DirectionsView(request,tob,id):
    business = BusinessProfile.objects.filter(id=id).first()
    return render(request,'inside/directionspage.html',{'business':business})

def logoutview(request):
    return render(request,'Registration/logout.html')

@login_required
def Dashboard(request,bizid):

    if request.user.id != bizid:
        messages.warning(request,"you dont have access to this dashboard")
        return redirect('home')

    else:
        buz = bizid
        businessId = BusinessProfile.objects.get(user_id=buz)
        recommended = Recommend.objects.filter(Recommended_company_id=buz)
        return render(request,'inside/dashboard.html',{'business':businessId,'recomandations':recommended})

def AboutPage(request):

    return render(request,'inside/about page.html')


def Editsite(request):

    if request.user.businesspro.type_of_business == "Club":
        return redirect('clubedithome')
    elif request.user.businesspro.type_of_business == "LiquorStore":
        return redirect('editliquorhome')
    elif request.user.businesspro.type_of_business ==  "Cosmetics":
        return redirect('cosmeticsedithome')
    elif request.user.businesspro.type_of_business == "Food":
        return redirect('Editfoodhome')
    elif request.user.businesspro.type_of_business == "Salon":
        return redirect('editsalonhome')

def VisitsiteView(request,typ,name):

    if typ == "Club":
        return redirect("clubhome",name=name)
    elif typ == "LiquorStore":
        return redirect("liquorhome",name=name)
    elif typ == "Cosmetics":
        return redirect("cosmeticshome",name=name)
    elif  typ == "Food":
        return redirect("foodhomepage",name=name)
    elif typ == "Salon":
        return redirect("salonhomepage",name=name)

def DomainView(request,typ,name):


    if typ == "Club":
        return redirect("clubhome",name=name)
    elif typ == "LiquorStore":
        return redirect("liquorhome",name=name)
    elif typ == "Cosmetics":
        return redirect("cosmeticshome",name=name)
    elif  typ == "Food":
        return redirect("foodhomepage",name=name)
    elif typ == "Salon":
        return redirect("salonhomepage",name=name)

def RecomendView(request):

    return render(request,'inside/recommend.html')


def NameSearchView(request):

    name = request.POST['business_name']
    bustype = request.POST['type']
    businesses = BusinessProfile.objects.filter(business_name__icontains=name).filter(type_of_business=bustype).order_by('-recommendations')

    return render(request,'inside/searchedmenu.html',{'businesses':businesses})





















from django.urls import path
from .views import EditSalonHome,EditSalonPrices,SalonHomepage,SalonPricespage,Saloncontacts,DeleteStyle

urlpatterns = [

    path("Edithome/",EditSalonHome,name="editsalonhome"),
    path("Editprices/",EditSalonPrices,name="editsalonprices"),
    path('Deletestyle',DeleteStyle,name='styledel'),


    path("<name>/home/",SalonHomepage,name="salonhomepage"),
    path("<name>/prices/",SalonPricespage,name="salonpricespage"),
    path("<name>/contacts/",Saloncontacts,name="saloncontactspage"),

    path("<name>",SalonHomepage,name="salonhomepage"),

]

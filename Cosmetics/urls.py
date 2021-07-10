from django.urls import path
from .views import EditCosmeticsHome,EditCosmeticsWork,CosmeticsContactPage,CosmeticsHomePageView,CosmeticsWorkPage,DeleteWork




urlpatterns = [

    path("<name>",CosmeticsHomePageView,name="cosmeticshome"),
    path("<name>/home/",CosmeticsHomePageView,name="cosmeticshome"),
    path("<name>/work/",CosmeticsWorkPage,name="cosmeticswork"),
    path("<name>/contact/",CosmeticsContactPage,name="cosmeticscontact"),


    path("Edithome/",EditCosmeticsHome,name="cosmeticsedithome"),
    path("Editwork/",EditCosmeticsWork,name="cosmeticseditwork"),
    path("Deletework/",DeleteWork,name="deletework"),
]

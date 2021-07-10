from django.urls import path
from .views import EditLiquorHome,EditLiquorSales,LiquorHomepage, LiquorSalespage,LiquorContacts,DeleteSaleItem


urlpatterns = [

    path("Edithome/",EditLiquorHome,name="editliquorhome"),
    path("Editsales/",EditLiquorSales,name="editliquorsales"),
    path("Deletesale",DeleteSaleItem,name="deletesale"),

    path("<name>",LiquorHomepage,name="liquorhome"),
    path("<name>/home/",LiquorHomepage,name="liquorhome"),
    path("<name>/sales/",LiquorSalespage,name="liquorsales"),
    path("<name>/contacts/",LiquorContacts,name="liquorcontacts"),








]

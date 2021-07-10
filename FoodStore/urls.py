from django.urls import path
from .views import EditFoodHome,EditFoodMenu,FoodHomePage,FoodContactPage,FoodMenu,DeleteMenuItem



urlpatterns = [

    path("<name>",FoodHomePage,name="foodhomepage"),

    path("<name>/home/",FoodHomePage,name="foodhomepage"),
    path("<name>/contact/",FoodContactPage,name="foodcontactpage"),
    path("<name>/menu/",FoodMenu,name="foodmenupage"),

    path("Edithome/",EditFoodHome,name="Editfoodhome"),
    path("Editmenu/",EditFoodMenu,name="Editfoodmenu"),
    path('Deletemenu/',DeleteMenuItem,name="deletemenu"),

]

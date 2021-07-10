from django.urls import path
from .views import signupView, HomeView, BusinessProfilesView, CustomerProfilesView, EditProfileView , CategoryMenu , SearchedView , DetailPageView, DirectionsView, logoutview, Dashboard, AboutPage
from .views import Editsite, VisitsiteView, DomainView, RecomendView, NameSearchView
from Responses.views import ReviewsView

urlpatterns = [
    path('accounts/signup/', signupView, name="signup"),
    path('', HomeView, name="home"),
    path('searchedbiz',NameSearchView,name="searchedname"),
    path('recommend',RecomendView,name="rec"),
    path('accounts/logout/',logoutview,name='logout'),
    path('profiles/business/', BusinessProfilesView, name='BusinessPro'),
    path('profiles/customer/', CustomerProfilesView, name='CustomerPro'),
    path('editmyprofile',EditProfileView,name="editprofile"),
    path('category/<cat>/',CategoryMenu,name='categorymenu'),
    path('searched/business/',SearchedView,name='searched'),
    path('details/<tob>/<id>/',DetailPageView,name='details'),
    path('directions/<tob>/<id>',DirectionsView,name='directions'),
    path('dashboard/<int:bizid>',Dashboard,name='dashboard'),
    path('pages/about',AboutPage,name="AboutPage"),
    path('Editsite',Editsite,name="editsite"),
    path('typ/name',DomainView),
    path('Visitsite/<typ>/<name>',VisitsiteView, name='sitevisit'),




]

from django.urls import path
from .views import ReviewsView, NearMapView

urlpatterns = [
    path('business/id=<int:business>/',ReviewsView,name='reviews'),
    path('showmap/<tob>',NearMapView,name='nearmap')
]

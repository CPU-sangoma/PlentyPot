from django.urls import path 
from .views import RecommendView



urlpatterns = [
    
    path('business/',RecommendView,name="recommend")
]

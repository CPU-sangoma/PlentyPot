from django.db import models
from django.conf import settings
from profiles.models import BusinessProfile

# Create your models here.


class Recommend(models.Model):
    
    Recommend_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("Recommended by"), on_delete=models.CASCADE,related_name="users")
    Recommended_company = models.ForeignKey(BusinessProfile,verbose_name=("Recommended Company"), on_delete=models.CASCADE,related_name="recommends")

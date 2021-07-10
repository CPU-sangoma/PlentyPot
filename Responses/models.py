from django.db import models
from django.conf import settings
from profiles.models import BusinessProfile
from PIL import Image 


# Create your models here.



class Reviews(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="reviews")
    reviewing = models.ForeignKey(BusinessProfile,on_delete=models.CASCADE, related_name="reviews")
    body = models.TextField()
    picture = models.ImageField(upload_to='reviewsmedia', height_field=None, width_field=None, max_length=None,null=True,blank=True,default="empty.jpg")
    time= models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)


    def save(self):
        super().save()
        
        img = Image.open(self.picture.path)
        
        if img.height > 400 or img.width > 400 :
            size = (400,400)
            img.thumbnail(size)
            img.save(self.picture.path)
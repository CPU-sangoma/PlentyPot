from django.db import models
from profiles.models import BusinessProfile


class FoodHomePageModel(models.Model):
    company = models.OneToOneField(BusinessProfile,on_delete=models.CASCADE,related_name="foodhome")
    BannerImage = models.ImageField(verbose_name="Upload an eye catching large picture to impress visitors", upload_to="Foodshop/Homepage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    welcomeMes = models.TextField(verbose_name="Write a warm welcome message for your visitors")

    item1pic = models.ImageField(verbose_name="Upload the first picture to display on your home page,usually a dish", upload_to="Foodshop/Homepage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    item1name = models.CharField(max_length=100,verbose_name=" the name of the first picture you were instructed to upload")
    item1description = models.TextField(verbose_name="a short description of the first picture you were instructed to upload")

    item2pic = models.ImageField(verbose_name="Upload the second picture to display on your home page,usually a dish", upload_to="Foodshop/Homepage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    item2name = models.CharField(max_length=100,verbose_name=" the name of the second picture you were instructed to upload")
    item2description = models.TextField(verbose_name="a short description of the second picture you were instructed to upload")

    item3pic = models.ImageField(verbose_name="Upload the third picture to display on your home page,usually a dish", upload_to="Foodshop/Homepage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    item3name = models.CharField(max_length=100,verbose_name=" the name of the third picture you were instructed to upload")
    item3description = models.TextField(verbose_name="a short description of the third picture you were instructed to upload")

    item4pic = models.ImageField(verbose_name="Upload the fourth picture to display on your home page,usually a dish", upload_to="Foodshop/Homepage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    item4name = models.CharField(max_length=100,verbose_name=" the name of the fourth picture you were instructed to upload")
    item4description = models.TextField(verbose_name="a short description of the fourth picture you were instructed to upload")

    item5pic = models.ImageField(verbose_name="Upload the fifth picture to display on your home page,usually a dish", upload_to="Foodshop/Homepage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    item5name = models.CharField(max_length=100,verbose_name=" the name of the fifth picture you were instructed to upload")
    item5description = models.TextField(verbose_name="a short description of the fifth picture you were instructed to upload")

    item6pic = models.ImageField(verbose_name="Upload the sixth picture to display on your home page,usually a dish", upload_to="Foodshop/Homepage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    item6name = models.CharField(max_length=100,verbose_name=" the name of the sixth picture you were instructed to upload")
    item6description = models.TextField(verbose_name="a short description of the sixth picture you were instructed to upload")

    item7pic = models.ImageField(verbose_name="Upload the seventh picture to display on your home page,usually a dish", upload_to="Foodshop/Homepage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    item7name = models.CharField(max_length=100,verbose_name=" the name of the seventh picture you were instructed to upload")
    item7description = models.TextField(verbose_name="a short description of the seventh picture you were instructed to upload")

    item8pic = models.ImageField(verbose_name="Upload the eighth picture to display on your home page,usually a dish", upload_to="Foodshop/Homepage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    item8name = models.CharField(max_length=100,verbose_name=" the name of the eighth picture you were instructed to upload")
    item8description = models.TextField(verbose_name="a short description of the eighth picture you were instructed to upload")
    status = models.BooleanField(default=True)
    PageComplete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.company}'

class FullMenuPageModel(models.Model):
    company = models.OneToOneField(BusinessProfile,on_delete=models.CASCADE,related_name="foodmenu")

    status = models.BooleanField(default=True)
    PageComplete = models.BooleanField(default=False)



class ActualMenuModel(models.Model):
    company = models.ForeignKey(BusinessProfile,on_delete=models.CASCADE,related_name="actualmenudata")
    menupic = models.ImageField(verbose_name="Upload the picture of the first item on your menu", upload_to="Foodshop/Foodmenu", height_field=None, width_field=None, max_length=None,null=True,blank=True)
    menudes = models.TextField(verbose_name="a short description of the first picture on your menu",null=True,blank=True)


    def __str__(self):
        return f'{self.company}'









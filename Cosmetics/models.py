from django.db import models
from profiles.models import BusinessProfile
# Create your models here.


class CosmeticsHomePage(models.Model):

    company = models.OneToOneField(BusinessProfile, on_delete=models.CASCADE, related_name="cosmeticshome")
    BannerImage = models.ImageField(verbose_name="Big picture for your home page to welcome your vistors", upload_to="Cosmetics/Homepage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    firstpic  =   models.ImageField(verbose_name="Upload image to make your home page interesting", upload_to="Cosmetics/Homepage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    secondpic = models.ImageField(verbose_name="Upload image to make your home page interesting", upload_to="Cosmetics/Homepage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    thirdpic = models.ImageField(verbose_name="Upload image to make your home page interesting", upload_to="Cosmetics/Homepage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    forthpic = models.ImageField(verbose_name="Upload image to make your home page interesting", upload_to="Cosmetics/Homepage", height_field=None, width_field=None, max_length=None,null=True,blank=False)

    fstworkpic = models.ImageField(verbose_name="show people some of your best works", upload_to="Cosmetics/Homepage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    fstworkdes= models.TextField(verbose_name="a little description about the first work picture")
    secworkpic = models.ImageField(verbose_name="show people some of your best works", upload_to="Cosmetics/Homepage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    secworkdes= models.TextField(verbose_name="a little description about the sec work picture")
    thirdworkpic = models.ImageField(verbose_name="show people some of your best works", upload_to="Cosmetics/Homepage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    thirdworkdes= models.TextField(verbose_name="a little description about the third work picture")

    fstteampic =  models.ImageField(verbose_name="the picture of the first team member", upload_to="Cosmetics/Homepage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    fstteamdes = models.TextField(verbose_name="a little description about the fst team member")
    secteampic =  models.ImageField(verbose_name="the picture of the second team member", upload_to="Cosmetics/Homepage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    secteamdes = models.TextField(verbose_name="a little description about the second team member")
    thirdteampic =  models.ImageField(verbose_name="the picture of the third team member", upload_to="Cosmetics/Homepage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    thirdteamdes = models.TextField(verbose_name="a little description about the third team member")
    status = models.BooleanField(default=True)
    PageComplete = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.company}'

class CosmeticsWork(models.Model):
    company = models.OneToOneField(BusinessProfile, on_delete=models.CASCADE, related_name="cosmeticswork")
    status = models.BooleanField(default=True)
    PageComplete = models.BooleanField(default=False)

class ActualCosWork(models.Model):
    company = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE, related_name="actualCosWork")
    Workpic = models.ImageField(verbose_name="Upload the picture of the first item on your menu", upload_to="Cosmetics/Workpage", height_field=None, width_field=None, max_length=None,null=True,blank=True)
    Workdes = models.TextField(verbose_name="a short description of the first picture on your menu",null=True,blank=True)






    def __str__(self):
        return f'{self.company}'


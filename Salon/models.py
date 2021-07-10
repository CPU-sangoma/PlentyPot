from django.db import models
from profiles.models import BusinessProfile
# Create your models here.


class SalonHomeModel(models.Model):

    company = models.OneToOneField(BusinessProfile, on_delete=models.CASCADE,related_name="salonhome")
    BannerImage = models.ImageField(verbose_name="upload an attractive banner image to impress visitors", upload_to="Salon/Home", height_field=None, width_field=None, max_length=None,null=True,blank=False)

    image1 = models.ImageField(verbose_name="upload an image to add style and a personal touch to your home page", upload_to="Salon/Home", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    image2 = models.ImageField(verbose_name="upload an attractive banner image to impress visitors", upload_to="Salon/Home", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    image3 = models.ImageField(verbose_name="upload an attractive banner image to impress visitors", upload_to="Salon/Home", height_field=None, width_field=None, max_length=None,null=True,blank=False)

    example1 = models.ImageField(verbose_name="upload an example of your best work", upload_to="Salon/Home", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    example2 = models.ImageField(verbose_name="upload an example of your best work", upload_to="Salon/Home", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    example3 = models.ImageField(verbose_name="upload an example of your best work", upload_to="Salon/Home", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    example4 = models.ImageField(verbose_name="upload an example of your best work", upload_to="Salon/Home", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    example5 = models.ImageField(verbose_name="upload an example of your best work", upload_to="Salon/Home", height_field=None, width_field=None, max_length=None,null=True,blank=False)

    team1pic = models.ImageField(verbose_name="upload a picture of the first team member", upload_to="Salon/Home", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    team1Name = models.CharField(verbose_name=" the name of the first team member",max_length=100)
    team1des = models.TextField(verbose_name="tell your visitors more about the first team member's speciality include contact info ")

    team2pic = models.ImageField(verbose_name="upload a picture of the second team member", upload_to="Salon/Home", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    team2Name = models.CharField(verbose_name=" the name of the second team member",max_length=100)
    team2des = models.TextField(verbose_name="tell your visitors more about the first team member's speciality include contact info ")

    team3pic = models.ImageField(verbose_name="upload a picture of the third team member", upload_to="Salon/Home", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    team3Name = models.CharField(verbose_name=" the name of the third team member",max_length=100)
    team3des = models.TextField(verbose_name="tell your visitors more about the third team member's speciality include contact info ")

    team4pic = models.ImageField(verbose_name="upload a picture of the fourth team member", upload_to="Salon/Home", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    team4Name = models.CharField(verbose_name=" the name of the fourth team member",max_length=100)
    team4des = models.TextField(verbose_name="tell your visitors more about the fourth team member's speciality include contact info ")
    status = models.BooleanField(default=True)
    PageComplete = models.BooleanField(default=False)

class SalonPricesModel(models.Model):
    company = models.OneToOneField(BusinessProfile, on_delete=models.CASCADE,related_name="salonprices",null=True)
    status = models.BooleanField(default=True)
    PageComplete = models.BooleanField(default=False)

class ActualSalonModel(models.Model):
    company = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE,related_name="actsalonprices",null=True)
    stylepic = models.ImageField(verbose_name="upload 1st pic of the styles you are offering", upload_to="Salon/Prices", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    styledes = models.TextField(verbose_name="full details of the first style you are offering, include the price and variations")


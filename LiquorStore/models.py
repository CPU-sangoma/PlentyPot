from django.db import models
from profiles.models import BusinessProfile



class LiquorHomePageModel(models.Model):

    bannerImage = models.ImageField(verbose_name="upload a big banner Image for your Home Page",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)

    wine1 = models.ImageField(verbose_name="first pic under wines/champagne",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    wine1des = models.TextField(verbose_name="price description for first wines/champagne pic", blank=False,null=True)
    wine2 = models.ImageField(verbose_name="second pic under wines/champagne",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    wine2des = models.TextField(verbose_name="price description for sec wines/champagne pic", blank=False,null=True)
    wine3 = models.ImageField(verbose_name="third pic under wines/champagne",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    wine3des = models.TextField(verbose_name="price description for third wines/champagne pic", blank=False,null=True)
    wine4 = models.ImageField(verbose_name="fourth pic under wines/champagne",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    wine4des = models.TextField(verbose_name="price description for fifth wines/champagne pic", blank=False,null=True)
    wine5 = models.ImageField(verbose_name="fifth pic under wines/champagne",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    wine5des = models.TextField(verbose_name="price description for fifth wines/champagne pic", blank=False,null=True)
    wine6 = models.ImageField(verbose_name="sixth pic under wines/champagne",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    wine6des = models.TextField(verbose_name="price description for sixth wines/champagne pic", blank=False,null=True)
    wine7 = models.ImageField(verbose_name="seventh pic under wines/champagne",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    wine7des = models.TextField(verbose_name="price description for seventh wines/champagne pic", blank=False,null=True)
    wine8 = models.ImageField(verbose_name="8th pic under wines/champagne",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    wine8des = models.TextField(verbose_name="price description for eighth wines/champagne pic", blank=False,null=True)



    company = models.OneToOneField(BusinessProfile,on_delete=models.CASCADE,related_name="liquorhome")
    beer1 = models.ImageField(verbose_name="first pic under beers and cider",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    beer1des = models.TextField(verbose_name="price description for first beers/ciders pic", blank=False,null=True)
    beer2 = models.ImageField(verbose_name="second pic under beers and cider",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    beer2des = models.TextField(verbose_name="price description for second beers/ciders pic ", blank=False,null=True)
    beer3 = models.ImageField(verbose_name="third pic under beers and cider",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    beer3des = models.TextField(verbose_name="price description for third beers/ciders pic ", blank=False,null=True)
    beer4 = models.ImageField(verbose_name="fourth pic under beers and cider",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    beer4des = models.TextField(verbose_name="price description for forth beers/ciders pic ", blank=False,null=True)
    beer5 = models.ImageField(verbose_name="fifth pic under beers and cider",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    beer5des = models.TextField(verbose_name="price description for fifth beers/ciders pic", blank=False,null=True)
    beer7 = models.ImageField(verbose_name="7th pic under beers and cider",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    beer7des = models.TextField(verbose_name="price description for seventh beers/ciders pic", blank=False,null=True)
    beer8 = models.ImageField(verbose_name="8th pic under beers and cider",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    beer8des = models.TextField(verbose_name="price description for eighth beers/ciders pic", blank=False,null=True)

    bottle1 = models.ImageField(verbose_name="first pic under Liquor/Spirits",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    bottle1des = models.TextField(verbose_name="price description for first Liquor/Spirits pic", blank=False,null=True)
    bottle2 = models.ImageField(verbose_name="second pic under Liquor/Spirits",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    bottle2des = models.TextField(verbose_name="price description for second Liquor/Spirits pic", blank=False,null=True)
    bottle3 = models.ImageField(verbose_name="third pic under Liquor/Spirits",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    bottle3des = models.TextField(verbose_name="price description for third Liquor/Spirits pic", blank=False,null=True)
    bottle4 = models.ImageField(verbose_name="fourth pic under Liquor/Spirits",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    bottle4des = models.TextField(verbose_name="price description for forth Liquor/Spirits pic", blank=False,null=True)
    bottle5 = models.ImageField(verbose_name="fifth pic under Liquor/Spirits",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    bottle5des = models.TextField(verbose_name="price description for fifth Liquor/Spirits pic", blank=False,null=True)
    bottle6 = models.ImageField(verbose_name="sixth pic under Liquor/Spirits",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    bottle6des = models.TextField(verbose_name="price description for sixth Liquor/Spirits pic", blank=False,null=True)
    bottle7 = models.ImageField(verbose_name="seventh pic under Liquor/Spirits",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    bottle7des = models.TextField(verbose_name="price description for seventh Liquor/Spirits pic", blank=False,null=True)
    bottle8 = models.ImageField(verbose_name="8th pic under Liquor/Spirits",upload_to="LiquorStore/LiquorHome/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    bottle8des = models.TextField(verbose_name="price description for eighth Liquor/Spirits pic", blank=False,null=True)
    status = models.BooleanField(default=True)
    PageComplete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.company}'

class LiquorSalesModel(models.Model):
    company = models.OneToOneField(BusinessProfile, on_delete=models.CASCADE,related_name="liquorsales")
    status = models.BooleanField(default=True)
    PageComplete = models.BooleanField(default=False)


class ActualLiqSales(models.Model):
    company = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE,related_name="ActualLiquor")
    salepic = models.ImageField(verbose_name="1st sale item",upload_to="LiquorStore/LiquorSale/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    saledes = models.TextField(verbose_name="sale description for item1", blank=False,null=True)



    def __str__(self):
        return f'{self.company}'

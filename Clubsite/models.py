from django.db import models
from profiles.models import BusinessProfile

# Create your models here.

class HomePageModel(models.Model):
    company = models.OneToOneField(BusinessProfile, on_delete=models.CASCADE,related_name="clubhome")
    Banner = models.ImageField(verbose_name="big banner image to be displayed on your home page",upload_to="club/HomePage/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    welcome_message = models.TextField(verbose_name="give you visitors a warm welcome",null=True,blank=False)
    about_club = models.TextField(verbose_name="about your club",null=True,blank=False)
    fstGpic = models.ImageField(verbose_name="fst gallery pic", upload_to="club/HomePage/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    secGpic = models.ImageField(verbose_name="sec gallery pic", upload_to="club/HomePage/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    trdGpic = models.ImageField(verbose_name="third gallery pic", upload_to="club/HomePage/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    frthGpic = models.ImageField(verbose_name="fourth gallery pic", upload_to="club/HomePage/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    fifGpic = models.ImageField(verbose_name="5th gallery pic", upload_to="club/HomePage/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    sixthGpic = models.ImageField(verbose_name="6th gallery pic", upload_to="club/HomePage/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    svthGpic = models.ImageField(verbose_name="7thGpic gallery pic", upload_to="club/HomePage/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    ResDjs1 = models.ImageField(verbose_name="Resdjs1 pic", upload_to="club/HomePage/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    Resdj1name = models.CharField(verbose_name="name of 1st dj", max_length=50)
    Resdj1pro = models.TextField(verbose_name="short profile of 1st resident dj")
    ResDjs2 = models.ImageField(verbose_name="Residentjs2 pic", upload_to="club/HomePage/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    Resdj2name = models.CharField(verbose_name="name of 2nd dj", max_length=50)
    Resdj2pro = models.TextField(verbose_name="short profile of 2nd resident dj")

    ResDjs3 = models.ImageField(verbose_name="Resdjs3 pic", upload_to="club/HomePage/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    Resdj3name = models.CharField(verbose_name="name of 3rd dj", max_length=50)
    Resdj3pro = models.TextField(verbose_name="short profile of 3rd resident dj")

    ResDjs4 = models.ImageField(verbose_name="Resdjs4 pic", upload_to="club/HomePage/", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    Resdj4name = models.CharField(verbose_name="name of 4rth dj", max_length=50)
    Resdj4pro = models.TextField(verbose_name="short profile of 4rth resident dj")
    status = models.BooleanField(default=1)
    PageComplete = models.BooleanField(default=False)
class TonightModel(models.Model):

    company= models.OneToOneField(BusinessProfile,on_delete=models.CASCADE,related_name="clubTonight")
    Currentpic1 = models.ImageField(verbose_name="show visitors whats happening now",upload_to="club/TonightPage", height_field=None, width_field=None, max_length=None, null=True,blank=True)
    Currentpic2 = models.ImageField(verbose_name="show visitors whats happening now",upload_to="club/TonightPage", height_field=None, width_field=None, max_length=None, null=True,blank=True)
    Currentpic3 = models.ImageField(verbose_name="show visitors whats happening now",upload_to="club/TonightPage", height_field=None, width_field=None, max_length=None, null=True,blank=True)
    Currentpic4 = models.ImageField(verbose_name="show visitors whats happening now",upload_to="club/TonightPage", height_field=None, width_field=None, max_length=None, null=True,blank=True)
    Specials = models.TextField()

    status = models.BooleanField(default=1)
    PageComplete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.company}'


class EventsPageModel(models.Model):

    company = models.OneToOneField(BusinessProfile, on_delete=models.CASCADE,related_name="clubEvents")
    MainEventpic = models.ImageField(upload_to="club/EventsPage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    name_of_main_event =  models.TextField(verbose_name="name of main event",null=True,blank=False)
    upcomming_event1 = models.ImageField(verbose_name="upcoming event 1",upload_to="club/EventsPage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    upcomming_event2 = models.ImageField(verbose_name="upcoming event 2",upload_to="club/EventsPage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    upcomming_event3 = models.ImageField(verbose_name="upcoming event 3",upload_to="club/EventsPage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    upcomming_event4 = models.ImageField(verbose_name="upcoming event 4",upload_to="club/EventsPage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    upcomming_event5 = models.ImageField(verbose_name="upcoming event 5",upload_to="club/EventsPage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    upcomming_event6 = models.ImageField(verbose_name="upcoming event 6",upload_to="club/EventsPage", height_field=None, width_field=None, max_length=None,null=True,blank=False)
    status = models.BooleanField(default=1)
    PageComplete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.company}'

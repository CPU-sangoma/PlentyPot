from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CusUser
from profiles.models import BusinessProfile, CustomerProfile
from Clubsite.models import EventsPageModel,TonightModel,HomePageModel


@receiver(post_save, sender=CusUser)
def CreatePro(sender, created, instance, **kwargs):
    if created:
        if instance.Account == "Customer":
            cus = CustomerProfile()
            cus.user = instance
            cus.save()

        else:
            bus = BusinessProfile()
            bus.user = instance
            bus.save()
            

from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


class CusUser(AbstractUser):
    choice_user = [
        ('Business', 'Business'),
        ('Customer', 'Customer'),
    ]



    Account = models.CharField(max_length=50, choices=choice_user, default="Customer")
    userpic = models.ImageField(upload_to="userpics", height_field=None, width_field=None, max_length=None,default="userpics/userpro.png")
    read_conditions = models.BooleanField(verbose_name="Are you sure youve read the terms and conditions of plentypot?",null=True,blank=False)



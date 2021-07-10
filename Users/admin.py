from django.contrib import admin
from .forms import CusUserCreation, CusUserChange
from .models import CusUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class CusAdmin(UserAdmin):
    form = CusUserChange
    add_form = CusUserCreation
    model = CusUser
    list_display = ['email', 'Account', 'last_name', 'is_staff', 'first_name']


admin.site.register(CusUser, CusAdmin)

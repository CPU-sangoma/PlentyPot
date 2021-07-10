from django.contrib import admin
from .models import EventsPageModel,HomePageModel,TonightModel
# Register your models here.

admin.site.register(HomePageModel)
admin.site.register(EventsPageModel)
admin.site.register(TonightModel)
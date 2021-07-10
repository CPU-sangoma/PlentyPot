from django.urls import path
from .views import EditClubHome,EditClubTonight, ClubHomepage, ClubTonightpage,ClubEventspage,ClubContacts
from .views import EditClubEvents

urlpatterns = [

    path("<name>",ClubHomepage,name="clubhome"),
    path("<name>/home/",ClubHomepage,name="clubhome"),
    path("<name>/tonight/",ClubTonightpage,name="clubtonight"),
    path("<name>/events/",ClubEventspage,name="clubevents"),
    path("<name>/contacts/",ClubContacts,name="clubcontacts"),

    path("Edithome/",EditClubHome,name="clubedithome"),
    path("Edittonight/",EditClubTonight,name="clubedittonight"),
    path("Editevents/",EditClubEvents,name="clubeditevents"),
    path("Editcontacts/",EditClubHome,name="clubeditcontacts"),




]

from django.urls import path
from .views import home, committee, important_dates, tracks, contact,about,call_for_papers
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", home, name="home"),
    path("committee/", committee, name="committee"),
    path("important_dates/", important_dates, name="important_dates"),
    path("tracks/", tracks, name="tracks"),
    path("contact/", contact, name="contact"),
    path("about/", about, name="about"),
    path("call_for_papers",call_for_papers,name="call_for_papers")
]

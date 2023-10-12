from django.urls import path
from .views import home, committee, important_dates, tracks, contact

urlpatterns = [
    path("", home, name="home"),
    path("committee/", committee, name="committee"),
    path("important_dates/", important_dates, name="important_dates"),
    path("tracks/", tracks, name="tracks"),
    path("contact/", contact, name="contact"),
]

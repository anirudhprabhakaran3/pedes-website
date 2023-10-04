from django.urls import path
from .views import home, committee, important_dates, tracks

urlpatterns = [
    path("", home, name="home"),
    path("committee/",committee, name="committee"),
    path("important_dates/", important_dates, name="important_dates"),
    path("tracks/", tracks, name="tracks")
    ]
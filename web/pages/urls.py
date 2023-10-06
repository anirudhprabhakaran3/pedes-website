from django.urls import path
from .views import home, committee


urlpatterns = [
    path("", home, name="home"),
    path("committee/",committee, name="committee"),
    ]
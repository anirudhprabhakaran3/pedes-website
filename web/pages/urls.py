from django.urls import path
from .views import home, committee, important_dates, tracks, contact,about,call_for_papers, speakers, event_details,accomodation, registration,paper_submission,keynote,tutorial,student_travel_award, reg_portal,travel_apply 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", home, name="home"),
    path("committee/", committee, name="committee"),
    path("important_dates/", important_dates, name="important_dates"),
    path("tracks/", tracks, name="tracks"),
    path("contact/", contact, name="contact"),
    path("about/", about, name="about"),
    path("call_for_papers",call_for_papers,name="call_for_papers"),
    path("speakers",speakers,name="speakers"),
    path("event_details/",event_details,name="event_details"),
    path("accomodation/",accomodation,name="accomodation"),
    path("registration/",registration,name="registration"),
    path("paper_submission/",paper_submission,name="paper_submission"),
    path("keynote/", keynote, name="keynote"),
    path("tutorial/", tutorial, name="tutorial"),
    path("student_travel_award/", student_travel_award, name="student_travel_award"),
    path("reg_portal/", reg_portal, name="reg_portal"),
    path("travel_apply/",travel_apply, name="travel_apply"),
]

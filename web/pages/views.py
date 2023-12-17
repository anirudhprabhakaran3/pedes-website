from django.shortcuts import render
from pages.models import Announcement


# Create your views here.


def home(request):
    announcements = Announcement.objects.all()

    args = {
        "announcements": announcements
    }

    return render(request, "pages/home.html", args)


# committee page

def committee(request):
    return render(request, "pages/committee.html")


def important_dates(request):
    return render(request, "pages/important_dates.html")


def tracks(request):
    return render(request, "pages/tracks.html")


def contact(request):
    return render(request, "pages/contact.html")


def about(request):
    return render(request, "pages/about.html")


def call_for_papers(request):
    return render(request, "pages/call_for_papers.html")


def speakers(request):
    return render(request, "pages/speakers.html")


def event_details(request):
    return render(request, "pages/event_details.html")


def accomodation(request):
    return render(request, "pages/accomodation.html")


def registration(request):
    return render(request, "pages/registration.html")


def paper_submission(request):
    return render(request, "pages/paper_submission.html")

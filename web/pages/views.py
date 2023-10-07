from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "pages/home.html")

#committee page

def committee(request):
    return render(request, "pages/committee.html")

def important_dates(request):
    return render(request, "pages/important_dates.html")


def tracks(request):
    return render(request, "pages/tracks.html")
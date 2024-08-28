from django.shortcuts import render
from pages.models import Announcement
from .forms  import  AttendeForm
# from .forms  import  AttendeForm, TickerTextForm
# from .models import TickerText
from django.shortcuts import render, redirect

# Create your views here.



def home(request):
    # announcements = Announcement.objects.all()

    # args = {
    #     "announcements": announcements
    # }
    # ticker_text = TickerText.objects.first()
    # return render(request, "pages/home.html",  {'ticker_text': ticker_text})
    return render(request,"pages/home.html")


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

def keynote(request):
    return render(request, "pages/keynote.html")

def tutorial(request):
    return render(request, "pages/tutorial.html")

def student_travel_award(request):
    return render(request, "pages/student_travel_award.html")


def travel_apply(request):
    return render(request, "pages/travel_apply.html")


def camera_paper(request):
    return render(request, "pages/camera_paper.html")

# IFRAME_MAPPINGS = {
#     ('IN', 'AUTHOR'): 'https://www.yepdesk.com/buy-tickets/66c4a47bc9e77c0001602f0b/private/n2tejimf0h',
#     ('IN', 'STUDENT'): 'https://www.yepdesk.com/buy-tickets/66c4a47bc9e77c0001602f0b/private/n2tejimf0h',
#     ('IN', 'PROF_ATN'): 'https://www.yepdesk.com/buy-tickets/66c4a47bc9e77c0001602f0b/private/n2tejimf0h',
#     ('IN', 'AUTHOR_ATN'): 'https://www.yepdesk.com/buy-tickets/66c4a47bc9e77c0001602f0b/private/n2tejimf0h',
#     ('IN', 'TUTORIAL'): 'https://www.yepdesk.com/buy-tickets/66c4a47bc9e77c0001602f0b/private/n2tejimf0h',
#     ('FR', 'AUTHOR'): 'https://www.yepdesk.com/buy-tickets/66c4a47bc9e77c0001602f0b/private/n2tejimf0h',
#     ('FR', 'STUDENT'): 'https://www.yepdesk.com/buy-tickets/66c4a47bc9e77c0001602f0b/private/n2tejimf0h',
#     ('FR', 'PROF_ATN'): 'https://www.yepdesk.com/buy-tickets/66c4a47bc9e77c0001602f0b/private/n2tejimf0h',
#     ('FR', 'AUTHOR_ATN'): 'https://www.yepdesk.com/buy-tickets/66c4a47bc9e77c0001602f0b/private/n2tejimf0h',
#     ('FR', 'TUTORIAL'): 'https://www.yepdesk.com/buy-tickets/66c4a47bc9e77c0001602f0b/private/n2tejimf0h',
    
#     # Add more combinations as needed
# }
def reg_portal(request):
    #  form_submitted = False
    # iframe_url = None
    # if request.method == 'POST':
    #     form = AttendeForm(request.POST)
    #     if form.is_valid():
    #         attende = form.save()
    #         # Get nationality and category from the form data
    #         nationality = attende.nationality
    #         category = attende.category
    #         # print(f"Nationality: {nationality}, Category: {category}")
    #         # Determine iframe URL based on nationality and category
    #         iframe_url = IFRAME_MAPPINGS.get((nationality, category))
    #         form_submitted = True
    # else:
    #     form = AttendeForm()
    return render(request,"pages/reg_portal.html")
    #  return render(request, "pages/reg_portal.html", {'form': form, 'form_submitted': form_submitted, 'iframe_url': iframe_url })

# def update_announcement(request):
#     if request.method == 'POST':
#         form = TickerTextForm(request.POST)
#         if form.is_valid():
#             # Retrieve or create the TickerText record with pk=1
#             ticker, created = TickerText.objects.get_or_create(pk=1)
#             ticker.text = form.cleaned_data['text']
#             ticker.is_active = form.cleaned_data['is_active']
#             ticker.save()
#             # Redirect to the home page after updating
#             return redirect('home')
#     else:
#         form = TickerTextForm()
    
#     # Render the form if not a POST request
#     ticker_text = TickerText.objects.first()  # Get the ticker text record
#     return render(request, "pages/update_announcement.html", {'form': form, 'ticker_text': ticker_text})
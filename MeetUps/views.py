from django.shortcuts import render ,get_list_or_404
from .models import Meetup
# Create your views here.

def index(request):
    MeetUps = Meetup.objects.all()
    return render(request, 'MeetUps/index.html', {
        'MeetUps': MeetUps
    })

def meetup_detials(request, meetup_slug):
    selected_meetup = Meetup.objects.get(slug=meetup_slug)
    selected_meetup = {
        'title': 'A First Meetup',
        'description': 'This is the first meetup!'
    }
    return render(request, 'MeetUps/meetup-details.html',{
        'meetup_title': selected_meetup.title,
        'meetup_description': selected_meetup.description
    })
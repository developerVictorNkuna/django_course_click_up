from django.urls import path

from . import views

urlpatterns = [
    path('MeetUps/', views.index, name='all-meetups'), #our-domain.com/MeetUps
    path('MeetUps/<str:meetup_slug>', views.meetup_detials, name='meetup-detail'), #our-domain.com/meetups/<dynamic-path-segment> 

]
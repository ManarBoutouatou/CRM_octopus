from django.conf.urls import url
from django.urls import path
from meetings.views import CalendarView, EventDeleteView, EventUpdateView, EventsListView, EventView
from . import views
from django.contrib.auth.decorators import login_required, permission_required
app_name= 'meetings'
urlpatterns = [
  
#calendar
 path('calendar', login_required(CalendarView.as_view()), name='calendar'),
 url(r'^event/new/$', login_required(views.event), name='event_new'),
	url(r'^event/edit/(?P<event_id>\d+)/$', login_required(views.event), name='event_edit'),

path('event_list', login_required(EventsListView.as_view()), name='event_list'),
path('eventdelete/<int:pk>/', login_required(EventDeleteView.as_view()), name="eventdelete"),
path('edit_event/<int:pk>/', login_required(EventUpdateView.as_view()), name="edit_event"),
path('event_view/<int:pk>/', login_required(EventView.as_view()), name="event_view"),
 
]

 



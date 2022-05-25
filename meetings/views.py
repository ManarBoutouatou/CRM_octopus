from datetime import datetime, timedelta, date
import calendar
from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from django.shortcuts import  redirect,render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.urls.base import reverse_lazy
from django.views import generic
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView, 
    FormView
)
from django.views.generic.edit import CreateView
from django.utils.safestring import mark_safe
from pprint import pprint
from contact.models import Company, Employee
from meetings.models import Event
from meetings.utils import Calendar 
from meetings.forms import EventForm
from .filters import Eventsfilter
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
import logging
# Create your views here.
class RedirectPermissionRequiredMixin(PermissionRequiredMixin,):
    login_url = reverse_lazy('core:index')
    def handle_no_permission(self):
        return redirect(self.get_login_url())
#calendar
class CalendarView(RedirectPermissionRequiredMixin, generic.ListView):
    model = Event
    template_name = 'calendar.html'
    permission_required= 'meetings.view_event'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('meetings:calendar'))
    return render(request, 'event_add.html', {'form': form})

class EventDeleteView(RedirectPermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Event
    template_name= "event_delete.html"
    success_message = "Event deleted successfully "
    success_url = reverse_lazy('meetings:calendar')

class EventsListView(RedirectPermissionRequiredMixin,ListView): 
    template_name= "event_list.html"
    model = Event
    permission_required= 'meetings.view_meet'
    def get_context_data(self, **kwargs):
        context = super(EventsListView, self).get_context_data(**kwargs)
        context["event_count"] =Event.objects.all().count()
        filters= Eventsfilter(self.request.GET, queryset=Event.objects.all().order_by('start_date'))
        context["events"] = filters.qs
        return context
    

class EventUpdateView(RedirectPermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Event
    form_class=  EventForm
    template_name = 'event_edit.html' 
    permission_required= 'meetings.change_meet'
    success_message = "Event updated successfully "
    success_url = reverse_lazy('meetings:event_list')
    def get_context_data(self, **kwargs):
        context = super(EventUpdateView, self).get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        context["employees"] = Employee.objects.all()
        return context

    def form_invalid(self, form):
        pprint(form.errors)
        return super().form_invalid(form)


class EventView(RedirectPermissionRequiredMixin,DetailView):
    model = Event
    template_name= "event_detail.html"
    permission_required= 'meetings.view_meet'

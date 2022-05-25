from django import forms
from django.forms import ModelForm, DateInput, TimeInput
from meetings.models import Event


class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    # widgets = {
    #   'start_date': DateInput(attrs={'type': 'date'}, format='%d-%m-%Y'),
    #   'start_time': TimeInput(attrs={'type': 'time'}, format='%H:%M:%S'),
    #   'end_time': TimeInput(attrs={'type': 'time'}, format='%H:%M:%S'),
    # }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    # self.fields['start_date'].input_formats = ('%d-%m-%Y')
    # self.fields['start_time'].input_formats = ('H:%M:%S',)
    # self.fields['end_time'].input_formats = ('H:%M:%S',) 



from django import forms
from .models import Event, Item 


class EventForm(forms.ModelForm):
  class Meta:
    model = Event 
    fields = ['name', 'desc', 'location', 'image', 'start_day', 'end_day', 'start_time', 'end_time']
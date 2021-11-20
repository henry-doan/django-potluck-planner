from django import forms
from .models import Event, Item 


class EventForm(forms.ModelForm):
  class Meta:
    model = Event 
    fields = ['image']
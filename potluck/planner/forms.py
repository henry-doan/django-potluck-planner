from django import forms
from .models import Event, Item, Contact


class EventForm(forms.ModelForm):
  class Meta:
    model = Event 
    fields = ['name', 'desc', 'location', 'image', 'start_day', 'end_day', 'start_time', 'end_time']


class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact 
    fields = ['name', 'email', 'msg', 'time_sent', 'msg_read']

class ItemForm(forms.ModelForm):
  class Meta:
    model = Item 
    fields = ['name', 'category']
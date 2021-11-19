from django.contrib import admin
from .models import Contact, Event, Item
# Register your models here.

admin.site.register(Contact)
admin.site.register(Event)
admin.site.register(Item)
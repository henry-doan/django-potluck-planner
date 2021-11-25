from django.shortcuts import render, redirect
from .models import Contact, Event, Item

# Create your views here.
def home(request):
  return render(request, 'planner/home.html')

def contact(request):
  if request.method == 'POST':
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    msg = request.POST.get('msg', '')
    contact = Contact(name=name, email=email, msg=msg)
    
    contact.save()
    # return render(request, 'planner/thank-you.html')
  return render(request, 'planner/contact.html')

def events(request):
  events = Event.objects.all()

  return render(request, 'planner/events.html', {'events': events})

def add_event(request):
  if request.method == 'POST':
    name = request.POST.get('name', '')
    desc = request.POST.get('desc', '')
    image = request.FILES["image"]
    location = request.POST.get('location', '')
    start_day = request.POST.get('start_day', '')
    end_day = request.POST.get('end_day', '')
    start_time = request.POST.get('start_time', '')
    end_time = request.POST.get('end_time', '')
    created_by = request.user.email
    event = Event(name=name, desc=desc, image=image, location=location, start_day=start_day, end_day=end_day, start_time=start_time, end_time=end_time, created_by=created_by)

    event.save()
    return redirect('events')
  return render(request, 'planner/addevent.html')

def event_details(request, pk):
  event = Event.objects.get(pk=pk)
  items = Item.objects.all()

  context = {
    'event': event,
    'items': items
  }

  return render(request, 'planner/eventdetails.html', context)
from django.shortcuts import render
from .models import Contact, Event

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

  # if request.method == 'POST':
  #   name = request.POST.get('name', '')
    
    
    # event.save()
  return render(request, 'planner/events.html', {'events': events})
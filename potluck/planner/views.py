from django.shortcuts import render, redirect
from .models import Contact, Event, Item
from .forms import EventForm, ContactForm, ItemForm

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
  entrees = Item.objects.filter(category = 'Entree', event = event)
  sides = Item.objects.filter(category = 'Side', event = event)
  desserts = Item.objects.filter(category = 'Dessert', event = event)
  drinks = Item.objects.filter(category = 'Drink', event = event)
  supplies = Item.objects.filter(category = 'Supplie', event = event)
  username = request.user.first_name + " " + request.user.last_name

  context = {
    'event': event,
    'items': items,
    'entrees': entrees,
    'sides': sides,
    'desserts': desserts,
    'drinks': drinks,
    'supplies': supplies,
    'username': username,
  }

  return render(request, 'planner/eventdetails.html', context)

def delete_event(request, id):
  event = Event.objects.get(id=id)

  if request.method == 'POST':
    event.delete()
    return redirect('events')

  return render(request, 'planner/deleteevent.html', { 'event': event })

def update_event(request, id):
  event = Event.objects.get(id=id)
  form = EventForm(request.POST or None, instance=event)

  if form.is_valid():
    form.save()
    return redirect('events')
  return render(request, 'planner/updateevent.html', { 'form': form, 'event': event } )

def contacts(request):
  contacts = Contact.objects.all()

  return render(request, 'planner/contacts.html', { 'contacts': contacts })

def delete_contact(request, id):
  contact = Contact.objects.get(id=id)

  if request.method == 'POST':
    contact.delete()
    return redirect('contacts')

  return render(request, 'planner/deletecontact.html', { 'contact': contact })

def contact_details(request, pk):
  contact = Contact.objects.get(pk=pk)

  context = {
    'contact': contact,
  }

  if contact.msg_read == False:
    contact.msg_read = True
    contact.save()

  return render(request, 'planner/contactdetails.html', context)

def update_contact(request, id):
  contact = Contact.objects.get(id=id)
  form = ContactForm(request.POST or None, instance=contact)

  if form.is_valid():
    form.save()
    return redirect('contacts')
  return render(request, 'planner/updatecontact.html', { 'form': form, 'contact': contact } )

def add_entree(request, pk):
  event = Event.objects.get(pk=pk)

  if request.method == 'POST':
    name = request.POST.get('name', '')
    category = 'Entree'
    userId = request.user.id
    created_by = request.user.first_name + " " + request.user.last_name
    item = Item(name=name, category=category, event=event, userId=userId, created_by=created_by)

    item.save()
    return redirect('event_details', pk=pk)
  return render(request, 'planner/addItem.html')

def add_side(request, pk):
  event = Event.objects.get(pk=pk)

  if request.method == 'POST':
    name = request.POST.get('name', '')
    category = 'Side'
    userId = request.user.id
    created_by = request.user.first_name + " " + request.user.last_name
    item = Item(name=name, category=category, event=event, userId=userId, created_by=created_by)

    item.save()
    return redirect('event_details', pk=pk)
  return render(request, 'planner/addItem.html')

def add_dessert(request, pk):
  event = Event.objects.get(pk=pk)

  if request.method == 'POST':
    name = request.POST.get('name', '')
    category = 'Dessert'
    userId = request.user.id
    created_by = request.user.first_name + " " + request.user.last_name
    item = Item(name=name, category=category, event=event, userId=userId, created_by=created_by)

    item.save()
    return redirect('event_details', pk=pk)
  return render(request, 'planner/addItem.html')

def add_drink(request, pk):
  event = Event.objects.get(pk=pk)

  if request.method == 'POST':
    name = request.POST.get('name', '')
    category = 'Drink'
    userId = request.user.id
    created_by = request.user.first_name + " " + request.user.last_name
    item = Item(name=name, category=category, event=event, userId=userId, created_by=created_by)

    item.save()
    return redirect('event_details', pk=pk)
  return render(request, 'planner/addItem.html')

def add_supplie(request, pk):
  event = Event.objects.get(pk=pk)

  if request.method == 'POST':
    name = request.POST.get('name', '')
    category = 'Supplie'
    userId = request.user.id
    created_by = request.user.first_name + " " + request.user.last_name
    item = Item(name=name, category=category, event=event, userId=userId, created_by=created_by)

    item.save()
    return redirect('event_details', pk=pk)
  return render(request, 'planner/addItem.html')


def update_item(request, id):
  item = Item.objects.get(id=id)

  if request.method == 'POST':
    name = request.POST.get('name', '')
    category = request.POST.get('category', '')
    updated_item = Item(id=item.id, name=name, category=category, userId=item.userId, event=item.event, created_by=item.created_by)

    updated_item.save()
    return redirect('event_details', pk=item.event.id)

  return render(request, 'planner/updateitem.html', {  'item': item } )

def delete_item(request, id):
  item = Item.objects.get(id=id)

  if request.method == 'POST':
    item.delete()
    return redirect('event_details', pk=item.event.id)

  return render(request, 'planner/deleteitem.html', { 'item': item })

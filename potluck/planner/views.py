from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'planner/home.html')

def contact(request):
  return render(request, 'planner/contact.html')
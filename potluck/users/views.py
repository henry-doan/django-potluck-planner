from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      first_name = form.cleaned_data.get('first_name')
      last_name = form.cleaned_data.get('last_name')
      messages.success(request, f'Welcome {first_name} {last_name}! You are logged in!')
      return redirect('login')
    else:
      print("not valid")
      print(form)
  else:
    form = RegistrationForm()
  return render(request, 'users/register.html', {'form': form})

# @login_required
from django.shortcuts import render, redirect
from .models import User, Profile 
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.dispatch import receiver

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      profile = Profile.objects.create(
          profile_name = request.user.get_username(),
          user_key = request.user,
      )
      profile.save()
      return redirect('index')
    else:
      error_message = 'Invalid credentials - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


class ProfileCreate(LoginRequiredMixin, CreateView):
  model = Profile
  fields = ['name', 'user_key']

def form_valid(self, form):
  # Assign the logged in user
  form.instance.user = self.request.user
  # Let the CreateView do its job as usual
  return super().form_valid(form)

def home(request):
  return render(request, 'home.html')

def community(request):
  return render(request, 'community.html')

@login_required
def profile(request):
  return render(request, 'profile.html')
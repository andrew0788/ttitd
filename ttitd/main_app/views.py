from django.shortcuts import render, redirect
from .models import User, Profile 
from .forms import ProfileForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.dispatch import receiver
from django.db.models.signals import post_save

# users = User.objects.all().select_related(Profile.user_key)

def get_profile(request):
    if request.method == 'GET':
        p_form = ProfileForm()
    return render(request, 'signup.html', {'p_form': p_form})

def signup(request):
  get_profile()
  error_message = ''
  if request.method == 'POST':
    user_form = UserCreationForm(request.POST)
    profile_form = ProfileForm(request.POST, instance=request.user.profile)
    if user_form.is_valid():
      user_form = form.save()
      login(request, user)
      # profile = Profile.objects.create(
      #     profile_name = request.user.get_username(),
      #     user_key = request.user,
      # )
      profile_form.save()
      print("this worked")
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

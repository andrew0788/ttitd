from django.shortcuts import render, redirect
from .forms import ProfileForm, UserForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.dispatch import receiver
from django.db import transaction
from django.db.models.signals import post_save
from .models import Profile, Drug, Effect, User_Drug_Effects, User

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'ttitd'

def home(request):
  return render(request, 'home.html')

@login_required
def profile(request):
    profile = request.user.profile
    user_id = request.user.id

    return render(request, 'profile/detail.html', {'user_id': user_id})

# To access user profile use:
# users = User.objects.all().select_related('profile')

def signup(request):
  if request.method == 'POST':
    user_form = UserCreationForm(request.POST)
    if user_form.is_valid():
      user = user_form.save()
      login(request, user)
      return redirect('/') #Update to route to the Profile Update view
    else:
      error_message = 'Invalid credentials -- try again'
  else:
    user_form = UserCreationForm()
  context = {'user_form': user_form}
  return render(request, 'registration/signup.html', context)

# @login_required
# def profile_update(request):
#     if request.method == 'POST':
#         profile_form = ProfileForm(request.POST)
#         if profile_form.is_valid():
#             user = profile_form.save()
#             return redirect('/')
#         else:
#             error_message = 'Invalid credentials -- try again'
#     else:
#         profile_form = ProfileForm()
#
#     return render(request, 'profile/profile_update.html', {'profile_form': profile_form})
#
# def update_profile(request, user_id):
#     user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
#     user.save()

@login_required
@transaction.atomic
def profile_update(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/')
        else:
            error_message = 'Invalid credentials -- try again'
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile/profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def substances_all(request):
  substance = Drug.objects.all()
<<<<<<< HEAD
  return render(request, 'substances/index.html', {
=======
  return render(request, 'substances/all.html', {
>>>>>>> b2b99c20c5f0051c037db54dc69ef6f4b7580c06
    'substance': substance
  })

def trips_all(request):
  return render(request, 'trips/index.html')


@login_required
def add_photo(request, drug_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, drug_id=drug_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', drug_id=drug_id)

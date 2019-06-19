from django.shortcuts import render, redirect
from .models import Profile, Drug, Effect, User_Drug_Effects
from .forms import ProfileForm, UserForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.dispatch import receiver
from django.db.models.signals import post_save

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'ttitd'

# Create your views here.

def home(request):
    return render(request, 'home.html')
    @login_required
    def profile(request):
        profile = Profile.objects.get(user_key=request.user)
        return render(request, 'profiles/detail.html', {'profile': profile})

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



@login_required
def profile_update(UpdateView):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if form.is_valid():
            user = profile_form.save()
            return redirect('/')
        else:
            error_message = 'Invalid credentials -- try again'
    else:
        profile_form = ProfileForm()
    context = {'profile_form': profile_form}
    return render(request, 'ProfileForm', context)


def substances_all(request):
  substance = Drug.objects.all()
  return render(request, 'substances/all.html', {
    'substance': substance
  })

def trips_all(request):
  return render(request, 'trips/all.html')


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

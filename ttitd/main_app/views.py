from django.shortcuts import render, redirect
from .models import User, Profile, Drug, Effect, User_Drug_Effects
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

p_user = User.id

# users = User.objects.all().select_related(Profile.user_key)

# def get_profile(request):
#     if request.method == 'GET':
#         p_form = ProfileForm()
#     return render(request, 'signup.html', {'p_form': p_form})

# def signup(request):
#   # get_profile()
#   error_message = ''
#   form = UserCreationForm()
#   if request.method == 'POST':
#     user_form = UserCreationForm(request.POST)
#     # profile_form = ProfileForm(request.POST, instance=request.user.profile)
#     if user_form.is_valid():
#       user_form = form.save()
#       login(request, user)
#       profile = Profile.objects.create(
#           profile_name = request.user.get_username(),
#           user_key = request.user,
#       )
#       profile.save()
#       print("this worked")
#       return redirect('index')
#     else:
#       error_message = 'Invalid credentials - try again'
#   form = UserCreationForm()
#   context = {'form': form, 'error_message': error_message}
#   return render(request, 'registration/signup.html', context)



S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'ttitd'

# Create your views here.

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    profile_form = ProfileForm(request.POST)
    if form.is_valid() and profile_form.is_valid():
      profile = profile_form.save()
      user = form.save()
      login(request, user)
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

def substances_all(request):
  d = Drug.objects.all()
  return render(request, 'substances/all.html', {
    'd': d
  })

def trips_all(request):
  return render(request, 'trips/all.html')


@login_required
def profile(request):
  p = Profile.objects.get(user_key=request.user)
  return render(request, 'profiles/detail.html', {'p': p})

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

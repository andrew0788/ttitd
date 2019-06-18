from django.shortcuts import render, redirect
from .models import User, Drug, Experience, Photo,
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'ttitd'

# Create your views here.

def signup(request):
    error_message = ''
    if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
        # This will add the user to the database
        user = form.save()
        # This is how we log a user in via code
        login(request, user)
        return redirect('index')
    else:
        error_message = 'Invalid credentials - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

def community(request):
  return render(request, 'community.html')

@login_required
def profile(request):
  return render(request, 'profile.html')

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

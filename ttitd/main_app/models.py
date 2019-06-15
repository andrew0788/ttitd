from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    profile_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    gender = models.CharField(max_length=15)
    age = models.SmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    bio = models.TextField(max_length=250)
    social_link = models.CharField(max_length=100)
    exp = models.IntegerField(default=0)
    # profile_photo = 
    # user_key =
    # ghost_key

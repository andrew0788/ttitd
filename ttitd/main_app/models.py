from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    profile_name = models.CharField(max_length=100)
    user_key = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    gender = models.CharField(max_length=15)
    age = models.IntegerField()
    weight = models.IntegerField()
    bio = models.TextField(max_length=250)
    social_link = models.CharField(max_length=100)
    exp = models.IntegerField(default=0)
    ghost_key = models.BooleanField(default=False)

    def __str__(self):
        if self.ghost_key == False:
            return self.profile_name
        else:
            return 'Anonymous'

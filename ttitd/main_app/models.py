from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user_key = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    gender = models.CharField(max_length=15)
    age = models.IntegerField()
    weight = models.IntegerField()
    bio = models.TextField(max_length=250)
    social_link = models.URLField('website', blank=True)
    exp = models.IntegerField(default=0)
    ghost_key = models.BooleanField(default=False)

    def __str__(self):
        if self.ghost_key == False:
            return self.profile_name
        else:
            return 'Anonymous'

class Drug(models.Model):
    name = models.CharField(max_length=100)
    discription = models.TextField(max_length=500)
    req_dose = models.CharField(max_length=150)
    view_count = models.IntegerField(default=0)
    effects = models.ManyToManyField('Effect', through='user_drug_effects')

#class Experince(models.Model):

class Effect(models.Model):
    name = models.CharField(max_length=50)

class user_drug_effects(models.Model):
    adj = models.ForeignKey('Effect', on_delete=models.CASCADE)
    drug = models.ForeignKey('Drug', on_delete=models.CASCADE)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)


class Photo(models.Model):
    url = models.CharField(max_length=200)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for drug_id: at {self.drug_id} @{self.url}"

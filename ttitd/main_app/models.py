from model_utils import Choices
from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user_key = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    gender = models.CharField(max_length=15)
    age = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
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
    description = models.TextField(max_length=500)
    req_dose = models.CharField(max_length=150)
    view_count = models.IntegerField(default=0)
    effects = models.ManyToManyField('Effect', through='User_Drug_Effects')


#class Experince(models.Model):

class Effect(models.Model):
    name = models.CharField(max_length=50)

class User_Drug_Effects(models.Model):
    adj = models.ForeignKey('Effect', on_delete=models.CASCADE)
    drug = models.ForeignKey('Drug', on_delete=models.CASCADE)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for drug_id: at {self.drug_id} @{self.url}"


class Trip_Report(models.Model):
    METHODS = Choices('ediable', 'smoked', 'oil/lotion', 'other')
    OTHER_DRUGS = Choices('Alcohol', 'Cannabis', 'Mushrooms', 'Payote')
    user_key = models.ForeignKey(User, on_delete=models.CASCADE)
    drug_key = models.ForeignKey(Drug, on_delete=models.CASCADE)
    text_content = models.TextField(max_length=250)
    date = models.DateField()
    method = models.CharField(max_length=1, choices=METHODS)
    other_drugs_taken = models.CharField(max_length= 4, choices=OTHER_DRUGS)
    effects = models.ManyToManyField(User_Drug_Effects)

class Report_Cat(models.Model):
    EXPERINCES = Choices('At the Park', 'At a Concert', 'At home', 'Medicinal', 'At Work', 'Other')
    category = models.CharField(max_length=1, choices=EXPERINCES)
    trip_report_key = models.ForeignKey(Trip_Report, on_delete=models.CASCADE)
    user_key = models.ForeignKey(User, on_delete=models.CASCADE)

class Report_Comment(models.Model):
    trip_report_key = models.ForeignKey(Trip_Report, on_delete=models.CASCADE)
    user_key = models.ForeignKey(User, on_delete=models.CASCADE)
    text_content = models.TextField(max_length=200)

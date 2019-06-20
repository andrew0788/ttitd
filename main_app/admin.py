from django.contrib import admin
from .models import Profile, Drug, Photo, Effect, User_Drug_Effects

admin.site.register(Profile)
admin.site.register(Drug)
admin.site.register(Photo)
admin.site.register(Effect)
admin.site.register(User_Drug_Effects)

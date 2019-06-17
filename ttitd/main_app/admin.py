from django.contrib import admin
from .models import Profile, Drug, Effect #Experience, Photo



admin.site.register(Profile)
admin.site.register(Drug)
#admin.site.register(Experience)
#admin.site.register(Photo)
admin.site.register(Effect)

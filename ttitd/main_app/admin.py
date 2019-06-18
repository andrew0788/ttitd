from django.contrib import admin
from .models import Profile, Drug, Photo, Effect, user_drug_effects

admin.site.register(Profile)
admin.site.register(Drug)
admin.site.register(Photo)
admin.site.register(Effect)
admin.site.register(user_drug_effects)

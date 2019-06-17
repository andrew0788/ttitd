from django.contrib import admin
from .models import User, Drug, Experience, Photo

admin.site.register(User)
admin.site.register(Drug)
admin.site.register(Experience)
admin.site.register(Photo)

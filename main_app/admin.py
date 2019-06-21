from django.contrib import admin
from .models import Profile, Drug, Photo, Effect, User_Drug_Effects, Trip_Report, Report_Cat, Report_Comment, TripReportPhoto, ProfilePhoto

admin.site.register(Profile)
admin.site.register(Drug)
admin.site.register(Photo)
admin.site.register(Effect)
admin.site.register(User_Drug_Effects)
admin.site.register(Trip_Report)
admin.site.register(Report_Cat)
admin.site.register(Report_Comment)
admin.site.register(TripReportPhoto)
admin.site.register(ProfilePhoto)

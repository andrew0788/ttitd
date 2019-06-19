from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
    path('profiles/detail', views.profile, name='profile'),
    path('profiles/profile_update', views.profile_update, name="profile_update"),
    path('substances/index', views.substances_all, name='substances_all'),
    path('trips/index', views.trips_all, name='trips_all'),
]

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('substances/all', views.substances_all, name='substances_all'),
    path('substances/index', views.substances_all, name='substances_all'),
    # delete below
    path('trips/detail', views.trips_detail, name='trips_detail'),
    # delete above
    path('trips/index', views.trips_all, name='trips_all'),
    path('profile/detail', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
]

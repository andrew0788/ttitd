from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profiles/detail', views.profile, name='profile'),
    path('cats/<int:pk>/update/', forms..as_view(), name='profile_update'),
    path('substances/all', views.substances_all, name='substances_all'),
    path('trips/all', views.trips_all, name='trips_all'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
]

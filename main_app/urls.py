from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('substances/index', views.substances_index, name='substances_index'),
    path('substances/<int:d_id>/detail/', views.substances_detail, name='substances_detail'),
    path('trips/all', views.trips_all, name='trips_all'),
    path('trips/index', views.trips_all, name='trips_all'),
    path('profile/detail', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('profile/<int:pk>/delete/', views.ProfileDelete, name='profile_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
]

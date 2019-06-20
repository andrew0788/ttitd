from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< Updated upstream:main_app/urls.py
=======
    path('profiles/detail', views.profile, name='profile'),
    path('profiles/profile_update', views.profile_update, name="profile_update"),
>>>>>>> Stashed changes:ttitd/main_app/urls.py
    path('substances/all', views.substances_all, name='substances_all'),
    path('substances/index', views.substances_all, name='substances_all'),
    path('trips/all', views.trips_all, name='trips_all'),
    path('trips/index', views.trips_all, name='trips_all'),
    path('profile/detail', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
]

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('substances/index', views.substances_index, name='substances_index'),
    path('subtances/detail', views.substances_detail, name='substances_detail'),
    path('substances/<int:d_id>/detail/', views.substances_detail, name='substances_detail'),
    path('trips/index', views.trips_all, name='trips_all'),
    path('trips/experiences', views.experiences, name='experiences'),
    path('trips/<int:pk>/delete', views.TripDelete.as_view(), name='trip_delete'),
    path('trips/<int:trip_id>/create', views.trips_create, name='trip_create'),
    path('trips/<int:pk>/update', views.TripUpdate.as_view(), name='trip_update'),
    path('trips/<int:report_id>/detail/', views.report_detail, name='report_detail'),
    path('profile/detail', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
]

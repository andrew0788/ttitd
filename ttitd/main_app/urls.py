from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('community/', views.community, name='community'),
    path('profile/', views.profile, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/<int:user_id>/', views.ProfileCreate, name='profile_create')
]

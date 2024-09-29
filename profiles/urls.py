from . import views
from django.urls import path

urlpatterns = [
    path('profile/', views.view_profile, name='profile'),
]

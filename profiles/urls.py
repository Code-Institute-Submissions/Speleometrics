from . import views
from django.urls import path

urlpatterns = [
    path('<str:username>', views.view_profile, name='profile_page'),
    path('edit/<str:username>', views.edit_profile, name='profile_edit'),
]

from . import views as views_profile
from caves import views as views_cave
from django.urls import path

urlpatterns = [
    path('<str:username>', views_profile.view_profile, name='profile_page'),
    path('<str:username>/edit/', views_profile.edit_profile, name='profile_edit'),
    path('<str:username>/add-cave/', views_cave.add_cave, name='add_cave'),
]

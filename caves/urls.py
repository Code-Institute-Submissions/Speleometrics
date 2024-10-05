from . import views
from django.urls import path

urlpatterns = [
    path('', views.cave_list_table, name='home'),
    path('<str:username>/add-cave/', views.add_cave, name='add_cave'),
]

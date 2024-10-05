from . import views
from django.urls import path

urlpatterns = [
    path('', views.cave_list_table, name='home'),
]

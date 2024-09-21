from . import views
from django.urls import path

urlpatterns = [
    path('', views.CaveList.as_view(), name='home'),
]

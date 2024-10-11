from . import views
from django.urls import path

urlpatterns = [
    path('', views.display_statistics, name='home'),
    path('about/', views.render_about, name='about'),
]
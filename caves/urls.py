from . import views
from django.urls import path

urlpatterns = [
    path('', views.cave_list_table, name='home'),
    path('cave/<str:cave_name>', views.cave_page, name='cave_page'),
]

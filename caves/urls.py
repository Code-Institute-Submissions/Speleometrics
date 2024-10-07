from . import views
from django.urls import path

urlpatterns = [
    path('', views.search_caves, name='home'),
    path('cave/<str:cave_name>/', views.cave_page, name='cave_page'),
    path('cave/<str:cave_name>/edit/<str:username>', views.edit_cave, name='edit_cave'),
    path('cave/<str:cave_name>/delete/<str:username>', views.delete_cave, name='delete_cave'),
]

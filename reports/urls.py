from . import views
from django.urls import path

urlpatterns = [
    path('', views.search_report, name='reports_index'),
    path('<int:id>', views.report_page, name='report_page'),
    path('delete/<int:id>', views.delete_report, name='delete_report'),
]

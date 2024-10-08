from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Report

# Register your models here.
@admin.register(Report)
class ReportAdmin(SummernoteModelAdmin):

    list_display = ('reported_by', 'cave', 'cave_owner', 'reported_created_date')
    search_fields = ['reported_created_date', 'cave', 'reported_by', 'cave_owner']
    summernote_fields = ('inconsistency_details',)

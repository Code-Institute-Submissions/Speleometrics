from django.contrib import admin
from .models import Cave
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Cave)
class CaveAdmin(SummernoteModelAdmin):

    list_display = ('cave_name', 'user', 'geomorph_unit')
    search_fields = ['cave_name', 'user']
    summernote_fields = ('description',)

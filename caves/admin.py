from django.contrib import admin
from .models import Cave
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Cave)
class CaveAdmin(SummernoteModelAdmin):

    list_display = ('cave_name', 'author', 'geomorph_unit')
    search_fields = ['cave_name', 'author']
    # prepopulated_fields = {'slug': ('cave_name',)}
    summernote_fields = ('description',)

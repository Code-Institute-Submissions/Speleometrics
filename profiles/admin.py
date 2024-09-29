from django.contrib import admin
from .models import Profile
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class ProfileAdmin(SummernoteModelAdmin):

    list_display = ('user', 'bio')
    search_fields = ['profile_type', 'user']
    # prepopulated_fields = {'slug': ('cave_name',)}
    summernote_fields = ('bio',)

from django import forms
from django.forms import ModelForm
from .models import Profile

class ProfileForm(forms.ModelForm):
    """ 
    User profile form 
    """
    class Meta:
        model = Profile
        fields = ('email_for_contact', 'profile_type', 'bio')
        labels = {
            "email_for_contact": "Email for Communication",
            "profile_type": "Profile Type",
            "bio": "User Profile Summary"
        }

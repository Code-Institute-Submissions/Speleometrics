from django import forms
from django.forms import ModelForm
from .models import Profile

class ProfileForm(forms.ModelForm):
    """ 
    User profile form 
    """
    class Meta:
        """
        Form used on adding info to user profile
        """
        model = Profile
        fields = ('display_name', 'email_for_contact', 'profile_type', 'bio', 'image')
        labels = {
            "display_name": "Profile Name",
            "email_for_contact": "Email for Communication",
            "profile_type": "Profile Type",
            "bio": "User Profile Summary",
            "image": "Profile Image",
        }

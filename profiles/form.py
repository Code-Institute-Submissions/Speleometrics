from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
        """ 
        User profile form 
        """
    class Meta:
        model = Profile
        fields = ('email_for_contact', 'profyle_type', 'bio')
        labels = {
            "email_for_contact": "Email for Communication",
            "profyle_type": "Profile Type",
            "bio": "User Profile Summary"
        }



class ProfileForm(forms.ModelForm):
    """ form for user to create a profile """
    class Meta:
        model = Profile
        fields = ['image', 'display_name', 'bio']

        labels = {
            "image": "Profile Pic",
            "display_name": "Display Name",
            "bio": "Bio"

        }
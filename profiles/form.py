from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fileds = ('email_for_contact', 'profyle_type', 'bio')
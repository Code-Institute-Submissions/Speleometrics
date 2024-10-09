from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    """
    Add a report message box to identify inconsistencies in the database.
    This is done by a modal that will display a textbox.
    """
    class Meta:
        model = Report
        fields = ['inconsistency_details']
        labels = {
            'inconsistency_details': 
            'Describe the inconsistency on the cave data'
        }
        widgets = {
            'inconsistency_details': 
            forms.Textarea(attrs={
                'rows': 5,
                'cols': 40
            })
        }
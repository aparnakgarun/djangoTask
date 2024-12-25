from django import forms
from .models import Portfolio

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['projects', 'work_experience', 'education', 'certifications']
        widgets = {
            'projects': forms.Textarea(attrs={'rows': 4}),
            'work_experience': forms.Textarea(attrs={'rows': 4}),
            'education': forms.Textarea(attrs={'rows': 4}),
            'certifications': forms.Textarea(attrs={'rows': 4}),
        }

from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = [ 'name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'job_city','profile_image', 'file']
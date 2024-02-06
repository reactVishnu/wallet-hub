from django import forms
from .models import TextDetail


class TextDetailForm(forms.ModelForm):
    class Meta:
        model = TextDetail
        fields = ['first_name', 'last_name', 'aadhar_no', 'pan_no']

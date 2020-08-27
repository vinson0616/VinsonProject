from django import forms
from .models import Report


class ReportInfoForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['name', 'phone', 'address','school','major','type','identity_card1','identity_card2','graduate_photo']
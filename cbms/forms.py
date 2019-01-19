from django import forms
from .models import Costomer


class CostomerForm(forms.ModelForm):
    class Meta:
        model = Costomer
        fields = ['name', 'gender', 'age']

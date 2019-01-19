from django import forms
from .models import Costomer, History, Genre


class CostomerForm(forms.ModelForm):
    class Meta:
        model = Costomer
        fields = ['name', 'gender', 'age']

class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = ['costomer', 'genre', 'date', 'time',]
    costomer = forms.ModelChoiceField(
        queryset=Costomer.objects.all(),
        label='顧客名'
    )
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(),
        label='ジャンル'
    )

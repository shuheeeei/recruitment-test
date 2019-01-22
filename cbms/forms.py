from django import forms
from .models import Costomer, History, Genre
import datetime
from dateutil.relativedelta import relativedelta


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

class DateForm(forms.Form):
    date_now = datetime.datetime.now()
    date_before_one = date_now - relativedelta(months=1)
    date_before_two = date_now - relativedelta(months=2)
    date_before_three = date_now - relativedelta(months=3)

    month_now = str(date_now.year) + '年' + str(date_now.month) + '月'
    month_before_one = str(date_before_one.year) + '年' + str(date_before_one.month) + '月'
    month_before_two = str(date_before_two.year) + '年' + str(date_before_two.month) + '月'
    month_before_three = str(date_before_three.year) + '年' + str(date_before_three.month) + '月'

    date_choices = [
                        ('', '---------'),
                        (str(date_now.year) + '/' + str(date_now.month), month_now),
                        (str(date_before_one.year) + '/' + str(date_before_one.month), month_before_one),
                        (str(date_before_two.year) + '/' + str(date_before_two.month), month_before_two),
                        (str(date_before_three.year) + '/' + str(date_before_three.month), month_before_three,)
                    ]
    choice = forms.ChoiceField(label='請求月', choices=date_choices)

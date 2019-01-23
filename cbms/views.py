from django.shortcuts import render
from django.http import HttpResponse
from .models import Costomer, History, Genre
from django.shortcuts import redirect
from .forms import CostomerForm, HistoryForm, DateForm
import datetime
from dateutil.relativedelta import relativedelta
from django.db.models import Count, Sum

def index(request):
    params = {
            'title': 'CostomerBillingManagementSystem'
    }
    return render(request, 'cbms/index.html', params)

def costomers(request):
    data = Costomer.objects.all()
    params = {
            'title': 'Costomer List',
            'data': data,
    }
    return render(request, 'cbms/costomer_list.html', params)

def costomer_create(request):
    if request.method == 'POST':
        obj = Costomer()
        costomer = CostomerForm(request.POST, instance=obj)
        costomer.save()
        return redirect(to='/cbms/costomers')
    params = {
            'title': 'Costomer Create',
            'form': CostomerForm(),
    }
    return render(request, 'cbms/costomer_create.html', params)

def costomer_edit(request, num):
    obj = Costomer.objects.get(id=num)
    if request.method == 'POST':
        costomer = CostomerForm(request.POST, instance=obj)
        costomer.save()
        return redirect(to='/cbms/costomers')
    params = {
            'title': 'Costomer Edit',
            'id': num,
            'form': CostomerForm(instance=obj),
    }
    return render(request, 'cbms/costomer_edit.html', params)


def histories(request):
    data = History.objects.all()
    params = {
            'title': 'Lesson Histories',
            'data': data,
    }
    return render(request, 'cbms/lesson_history_list.html', params)

def history_create(request):
    if request.method == 'POST':
        form = HistoryForm(request.POST)
        if form.is_valid():
            obj = History()
            history = HistoryForm(request.POST, instance=obj)
            history.save()
            return redirect(to='/cbms/histories')
    params = {
            'title': 'History Resiter',
            'form': HistoryForm(),
    }
    return render(request, 'cbms/lesson_history_create.html', params)

def history_edit(request, num):
    obj = History.objects.get(id=num)
    form = HistoryForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            history = HistoryForm(request.POST, instance=obj)
            history.save()
            return redirect(to='/cbms/histories')
    params = {
            'title': 'History Edit',
            'id': num,
            'form': HistoryForm(instance=obj),
    }
    return render(request, 'cbms/lesson_history_edit.html', params)


def billing_list(request):
    if request.method == 'POST':
        select_year = request.POST['choice'].split('/')[0]
        select_month = request.POST['choice'].split('/')[1]

        billing_list = []
        #日付でHistoryからデータ抽出(顧客の重複あり)
        base_query = History.objects.filter(date__year=select_year, date__month=select_month)
        # 配列で受講済み顧客IDを取得
        costomer_ids = base_query.values_list('costomer', flat=True).distinct()
        costomer_ids_list = list(costomer_ids)
        #無受講の顧客抽出
        #全顧客IDの抽出
        all_costomer_ids = Costomer.objects.values_list('id', flat=True)
        all_costomer_ids_list = list(all_costomer_ids)
        non_active_costomer_ids = []
        non_active_costomer_ids = list(set(all_costomer_ids_list) -set(costomer_ids_list))
        costomer_ids_list += non_active_costomer_ids

        for costomer_id in costomer_ids_list:
            billing_dict = {}
            billing_dict['costomer_id'] = costomer_id
            costomer = Costomer.objects.get(id=costomer_id)
            billing_dict['costomer_name'] = costomer.name

            genre_ids = base_query.filter(costomer=costomer_id).values_list('genre', flat=True).order_by('genre').distinct()
            genre = ''
            for genre_id in genre_ids:
                gnr = Genre.objects.filter(id=genre_id).values()
                genre += gnr[0]['subject'] + '/'
            billing_dict['genre'] = genre
            genre_num = len(genre_ids)
            billing_dict['genre_num'] = genre_num
            total_lesson = base_query.filter(costomer=costomer_id).count()
            billing_dict['total'] = total_lesson

            english_time = base_query.filter(costomer=costomer_id).filter(genre=1).aggregate(Sum('time'))
            if english_time['time__sum']:
                english_total_time = english_time['time__sum']
            else:
                english_total_time = 0
            finance_time = base_query.filter(costomer=costomer_id).filter(genre=2).aggregate(Sum('time'))
            if finance_time['time__sum']:
                finance_total_time = finance_time['time__sum']
            else:
                finance_total_time = 0
            programing_time = base_query.filter(costomer=costomer_id).filter(genre=3).aggregate(Sum('time'))
            if programing_time['time__sum']:
                programing_total_time = programing_time['time__sum']
            else:
                programing_total_time = 0


            '''英語'''
            english_fees = Genre.objects.filter(subject='英語')
            english_total_billing = english_fees[0].base_fee + english_total_time * english_fees[0].charge_fee

            '''ファイナンス'''
            finance_fees = Genre.objects.filter(subject='ファイナンス')
            if finance_total_time > 50:
                finance_total_billing = finance_fees[0].base_fee + finance_total_time * finance_fees[0].charge_fee + (finance_total_time - 20) * (finance_fees[0].charge_fee - 800)
            elif finance_total_time > 20:
                finance_total_billing = finance_fees[0].base_fee + finance_total_time * finance_fees[0].charge_fee + (finance_total_time - 20) * (finance_fees[0].charge_fee - 500)
            else:
                finance_total_billing = finance_fees[0].base_fee + finance_total_time * finance_fees[0].charge_fee

            '''プログラミング'''
            programing_fees = Genre.objects.filter(subject='プログラミング')
            if programing_total_time > 50:
                programing_total_billing = programing_fees[0].base_fee + programing_total_time * programing_fees[0].charge_fee + (programing_total_time - 20) * (programing_fees[0].charge_fee - 1000)
            elif programing_total_time > 35:
                programing_total_billing = programing_fees[0].base_fee + programing_total_time * programing_fees[0].charge_fee + (programing_total_time - 20) * (programing_fees[0].charge_fee - 700)
            elif programing_total_time > 20:
                programing_total_billing = programing_fees[0].base_fee + programing_total_time * programing_fees[0].charge_fee + (programing_total_time - 20) * (programing_fees[0].charge_fee - 500)
            else:
                programing_total_billing = programing_fees[0].base_fee + programing_total_time * programing_fees[0].charge_fee

            total_billing = english_total_billing +finance_total_billing + programing_total_billing
            billing_dict['total_billing'] = total_billing

            billing_list.append(billing_dict.copy())

        params = {
                'title': 'Billing List',
                'form': DateForm(),
                'billings': billing_list,
        }
    else:
        params = {
                'title': 'Billing List',
                'form': DateForm(),
        }
    return render(request, 'cbms/billing_list.html', params)

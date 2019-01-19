from django.shortcuts import render
from django.http import HttpResponse
from .models import Costomer, History, Genre
from django.shortcuts import redirect
from .forms import CostomerForm, HistoryForm


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
    if request.method == 'POST':
        history = HistoryForm(request.POST, instance=obj)
        history.save()
        return redirect(to='/cbms/histories')
    params = {
            'title': 'History Edit',
            'id': num,
            'form': HistoryForm(instance=obj),
    }
    return render(request, 'cbms/lesson_history_edit.html', params)

from django.shortcuts import render
from django.http import HttpResponse
from .models import Costomer
from django.shortcuts import redirect
from .forms import CostomerForm


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

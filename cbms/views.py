from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params = {
            'title': 'CostomerBillingManagementSystem'
    }
    return render(request, 'cbms/index.html', params)

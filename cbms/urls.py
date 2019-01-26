from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('costomers/', views.costomers, name='costomers'),
    path('costomers/create/', views.costomer_create, name='costomer_create'),
    path('costomers/edit/<int:num>', views.costomer_edit, name='costomer_edit'),
    path('histories/', views.histories, name='histories'),
    path('histories/create', views.history_create, name='history_create'),
    path('histories/edit/<int:num>', views.history_edit, name='history_edit'),
    path('billings', views.billing_list, name='billing'),
    path('reports', views.report, name='report'),
]

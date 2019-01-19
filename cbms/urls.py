from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('costomers/', views.costomers, name='costomers'),
    path('costomers/create/', views.costomer_create, name='costomer_create'),
    path('costomers/edit/<int:num>', views.costomer_edit, name='costomer_edit'),
]

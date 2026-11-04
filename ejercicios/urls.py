from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ejercicios, name='lista_ejercicios'),
]
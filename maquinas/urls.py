from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_maquinas, name='lista_maquinas'),
]
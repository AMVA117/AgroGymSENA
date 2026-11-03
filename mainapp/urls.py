from django.urls import path
from . import views

urlpatterns = [
    # Ruta raíz de la app mainapp (la página de inicio)
    path('', views.index, name='index'),
]
from django.urls import path
from django.views.generic import TemplateView

app_name = 'mainapp'

urlpatterns = [
    # Esto carga directamente la página de inicio (index.html) de tu compañera sin depender de views.py
    path('', TemplateView.as_view(template_name='mainapp/index.html'), name='inicio'),
]
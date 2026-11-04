from django.urls import path
from . import views

app_name = 'usuarios'  # <--- Esto es obligatorio para que reconozca 'usuarios:registro'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'), # <--- Asegúrate de tener esta ruta
]
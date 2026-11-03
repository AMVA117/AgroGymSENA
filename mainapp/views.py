from django.shortcuts import render

# Vista para la página de inicio del sistema
def index(request):
    """
    Esta función procesa la petición web (request) 
    y devuelve renderizada la plantilla index.html
    """
    return render(request, 'mainapp/index.html')
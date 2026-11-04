from django.shortcuts import render

# ==============================================================================
# VISTA: Página de Inicio / Menú Principal
# ==============================================================================
def inicio(request):
    """
    Renderiza la vista del menú principal de AgroGym con los accesos 
    a máquinas y ejercicios.
    """
    return render(request, 'mainapp/inicio.html')
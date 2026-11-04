from django.shortcuts import render

# ==============================================================================
# VISTA: Listado Básico de Máquinas (Datos Estáticos)
# ==============================================================================
def lista_maquinas(request):
    # Lista de prueba simulando los equipos del gimnasio del SENA
    maquinas_prueba = [
        {'nombre': 'Prensa de Piernas', 'descripcion': 'Ideal para cuádriceps y glúteos.', 'estado': 'Disponible'},
        {'nombre': 'Caminadora Eléctrica', 'descripcion': 'Excelente para entrenamiento cardiovascular.', 'estado': 'Disponible'},
        {'nombre': 'Máquina de Poleas', 'descripcion': 'Versátil para tren superior y espalda.', 'estado': 'En Mantenimiento'},
    ]
    
    return render(request, 'maquinas/lista_maquinas.html', {'maquinas': maquinas_prueba})
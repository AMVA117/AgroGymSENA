from django.shortcuts import render

# ==============================================================================
# VISTA: Listado Básico de Ejercicios (Datos Estáticos)
# ==============================================================================
def lista_ejercicios(request):
    # Lista de prueba simulando los ejercicios disponibles
    ejercicios_prueba = [
        {'nombre': 'Sentadilla Libre', 'grupo_muscular': 'Piernas y Glúteos', 'dificultad': 'Media'},
        {'nombre': 'Press de Banca', 'grupo_muscular': 'Pecho y Tríceps', 'dificultad': 'Media'},
        {'nombre': 'Dominadas', 'grupo_muscular': 'Espalda y Bíceps', 'dificultad': 'Alta'},
    ]
    
    return render(request, 'ejercicios/lista_ejercicios.html', {'ejercicios': ejercicios_prueba})
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# 1. Vista para registrar un nuevo usuario
def registro_view(request):
    if request.method == 'POST':  # Si el usuario envió el formulario lleno
        form = UserCreationForm(request.POST)
        if form.is_valid():  # Si los datos cumplen con las reglas de seguridad de Django
            user = form.save()  # Guarda el nuevo usuario en la base de datos
            login(request, user)  # Inicia sesión automáticamente después de registrarse
            messages.success(request, "¡Cuenta creada con éxito!")
            return redirect('login')  # Redirige al usuario hacia la vista de login
        else:
            messages.error(request, "Por favor, corrige los errores en el formulario.")
    else:  # Si el usuario recién entra a la página (método GET)
        form = UserCreationForm()
    
    return render(request, 'usuarios/registro.html', {'form': form})


# 2. Vista para el inicio de sesión (Login)
def login_view(request):
    if request.method == 'POST':  # Cuando el usuario presiona "Iniciar Sesión"
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():  # Verifica que el usuario y contraseña sean correctos
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)  # Autentica las credenciales
            if user is not None:
                login(request, user)  # Crea la sesión activa para el usuario
                messages.success(request, f"¡Bienvenido, {username}!")
                return redirect('mainapp:inicio')  # Redirige a la página principal del proyecto
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:  # Si entra por primera vez a la página de login
        form = AuthenticationForm()
        # Añadimos clases de Bootstrap directamente a los campos de Django para que coincidan con tu diseño visual
        form.fields['username'].widget.attrs.update({'class': 'form-control bg-light border-start-0', 'placeholder': 'usuario@soy.sena.edu.co'})
        form.fields['password'].widget.attrs.update({'class': 'form-control bg-light border-start-0', 'placeholder': '••••••'})

    return render(request, 'usuarios/login.html', {'form': form})


# 3. Vista para cerrar sesión (Logout)
def logout_view(request):
    logout(request)  # Cierra la sesión activa del usuario
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect('login')  # Devuelve al usuario a la pantalla de login
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


# Formulario de inicio de sesión
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.EmailInput(attrs={
            "placeholder": "usuario@soy.sena.edu.co",
            "autocomplete": "email",
        })
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            "placeholder": "••••••",
            "autocomplete": "current-password",
        }),
    )


# Formulario de registro (el correo se usa como nombre de usuario)
class RegistroForm(UserCreationForm):
    email = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={"placeholder": "usuario@soy.sena.edu.co"}),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "email")
        labels = {"first_name": "Nombres", "last_name": "Apellidos"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].label = "Contraseña"
        self.fields["password2"].label = "Confirmar contraseña"

    # Evita correos repetidos
    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if User.objects.filter(username__iexact=email).exists():
            raise forms.ValidationError("Ya existe una cuenta con este correo.")
        return email

    # Guarda el correo también como username
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
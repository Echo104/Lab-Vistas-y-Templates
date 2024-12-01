from django import forms
from .models import Usuario,Libro,Reseña

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=[
            'user'
        ]
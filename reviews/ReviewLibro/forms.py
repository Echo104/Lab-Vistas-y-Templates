from django import forms
from .models import Usuario,Libro,Reseña

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=[
            'user'
        ]

class LibroForm(forms.ModelForm):
    class Meta:
        model=Libro
        fields=[
            'titulo',
            'autor',
            'fecha_publicacion',
            'genero'
        ]

class ReseñaForm(forms.ModelForm):
    class Meta:
        model=Reseña
        fields=[
            'libro',
            'usuario',
            'calificacion',
            'comentario'
        ]
from django.shortcuts import render
from .forms import UsuarioForm,LibroForm,ReseñaForm
from .models import Usuario,Libro,Reseña
# Create your views here.
def myHomeView(request):
    return render(request,'reviews/inicio.html',)

def UsuarioCreateView(request):
    form=UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=UsuarioForm()
    
    usuarios=Usuario.objects.all()
    context={
        'form':form,
        'usuarios':usuarios
    }
    return render(request,'reviews/UsuarioCreate.html',context)

def LibroCreateView(request):
    form=LibroForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=LibroForm()
    
    libros=Libro.objects.all()
    context={
        'form':form,
        'libros':libros
    }
    return render(request,'reviews/LibroCreate.html',context)

def ReseñaCreateView(request):
    form=ReseñaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=ReseñaForm()
    
    resenas=Reseña.objects.all()
    context={
        'form':form,
        'resenas':resenas
    }
    return render(request,'reviews/ReseñaCreate.html',context)
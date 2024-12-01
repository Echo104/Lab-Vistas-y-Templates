from django.shortcuts import render
from .forms import UsuarioForm,LibroForm,ReseñaForm
# Create your views here.
def myHomeView(request):
    return render(request,'reviews/inicio.html',)

def UsuarioCreateView(request):
    form=UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=UsuarioForm()
    
    context={
        'form':form
    }
    return render(request,'reviews/UsuarioCreate.html',context)

def LibroCreateView(request):
    form=LibroForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=LibroForm()
    
    context={
        'form':form
    }
    return render(request,'reviews/LibroCreate.html',context)

def ReseñaCreateView(request):
    form=ReseñaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=ReseñaForm()
    
    context={
        'form':form
    }
    return render(request,'reviews/ReseñaCreate.html',context)
from django.shortcuts import render
from .forms import UsuarioForm
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
from django.shortcuts import render

# Create your views here.
def myHomeView(request):
    return render(request,'reviews/inicio.html',)
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')
     
def proyectos(request):
    return render(request, 'proyectos.html')

def certificados(request):
    return render(request, 'certificados.html')

def blog(request):
    return render(request, 'blog.html')

def contacto(request):
    return render(request, 'contacto.html')


from django.http import HttpResponse
from .models import Estudiantes
from django.shortcuts import render


# Create your views here.
def saludo(request):
    return HttpResponse("Buenas tardes a TODOS---")

def despedir(request):
    return HttpResponse("Hasta la vista Babys---")

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def inicio(request):
    return render(request, 'paginas/inicio.html')

def servicios(request):
    return render(request, 'paginas/servicios.html')

def contacto(request):
    return render(request, 'paginas/contacto.html')

def estudiantes(request):
    estudiantes = Estudiantes.objects.all()
    data={
    'estudiantes':estudiantes
    }
    return render(request, 'estudiantes/index.html', data)

def crear(request):
    return render(request, 'estudiantes/crear.html')

def editar(request):
    return render(request, 'estudiantes/editar.html')

def formulario(request):
    return render(request, 'estudiantes/formulario.html')
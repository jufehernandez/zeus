from django.http import HttpResponse
from .models import Estudiantes
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EstudiantesForm

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
    formulario = EstudiantesForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('estudiantes')
    return render(request, 'estudiantes/crear.html', {'formulario': formulario})

def editar(request, id):
    estudianteE = get_object_or_404(Estudiantes, id=id)

    if request.method == "POST":
        formulario = EstudiantesForm(request.POST, request.FILES, instance=estudianteE)
        if formulario.is_valid():
            formulario.save()
            return redirect('estudiantes')
    else:
        formulario = EstudiantesForm(instance=estudianteE)

    return render(request, 'estudiantes/editar.html', {'formulario': formulario})


def formulario(request):
    return render(request, 'estudiantes/formulario.html')

def eliminar(request, id):
    estudianteD = get_object_or_404(Estudiantes, id=id)
    if request.method == "POST":
        estudianteD.delete()
    return redirect('estudiantes')
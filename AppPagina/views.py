from django.http import HttpResponse

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
    return render(request, 'estudiantes/index.html')
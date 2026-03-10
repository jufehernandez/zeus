from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('saludo/', views.saludo, name='saludo'),
    path('despedir/', views.despedir, name='despedir'),
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('crear/', views.crear, name='crear'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('formulario/', views.formulario, name='formulario'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
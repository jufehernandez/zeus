from django.urls import path
from . import views

urlpatterns = [
    path('saludo/', views.saludo, name='saludo'),
    path('despedir/', views.despedir, name='despedir'),
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
]
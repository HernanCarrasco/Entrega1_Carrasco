from django.urls import path    
from AppFulvito.views import *

urlpatterns = [
    
    path("crear_curso/", crear_curso, name="crear_curso"),
    path("", inicio, name="inicio"),
    path("cursos/", cursos, name="cursos"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("profesores/", profesores, name="profesores"),
    path("entregables/", entregables, name="entregables"),
    path('Familia/', mostrar_fam, name="familia"),
    path('busqueda_comision/', busqueda_comision, name="busqueda_comision"),
    path('buscar/', buscar, name="buscar"),
    
]
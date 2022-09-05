from django.urls import path    
from AppFulvito.views import *

urlpatterns = [
    
    path("crear_curso/", crear_curso, name="crear_curso"),
    path("", inicio, name="inicio"),
    path("cursos/", cursos, name="cursos"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("profesores/", profesores, name="profesores"),
    path("entregables/", entregables, name="entregables"),
    path('Crear_Familiar1/', crear_fam1, name="familiar1"),
    path('Crear_Familiar2/', crear_fam2, name="familiar2"),
    path('Crear_Familiar3/', crear_fam3, name="familiar3"),
    path('Familia/', mostrar_fam, name="familia"),
    path('busqueda_comision/', busqueda_comision, name="busqueda_comision"),
    path('buscar/', buscar, name="buscar"),
    
]
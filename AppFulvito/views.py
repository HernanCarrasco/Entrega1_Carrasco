from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppFulvito.forms import * 

lista=[]

def mostrar_fam(request):
    dict_cont={'lista':lista}
    return render (request, 'AppProyecto/Familia.html', dict_cont)



def inicio(request):
    return render (request, "AppProyecto/inicio.html")

def cursos(request):  # Idear como mostrar la lista de Cursos
    return render (request, "AppProyecto/cursos.html")


def estudiantes(request): # Idear como mostrar la lista de Estudiantes
    return render (request, "AppProyecto/estudiantes.html")

def profesores(request):  # Idear como mostrar la lista de Profesores
    return render (request, "AppProyecto/profesores.html")

def entregables(request):  # Idear como mostrar la lista de Entregables
    return render (request, "AppProyecto/entregables.html")



def crear_curso(request):

    if request.method == "POST":

        formulario_user = EquipoForm(request.POST)

        if formulario_user.is_valid():
            info=formulario_user.cleaned_data
            nombredelcurso=info["nombre"]
            comisiondelcurso=info["comision"]
            curso=Equipo(nombre=nombredelcurso, comision=comisiondelcurso)
            curso.save()
            return render (request, "AppProyecto/inicio.html", {'mensaje': "Curso Creado!"})
    else:
        formulario_user=EquipoForm()
        return render (request, "AppProyecto/crear_curso.html", {"formulario":formulario_user})

def busqueda_comision(request):
    return render (request, "AppProyecto/busqueda_comision.html")
    
def buscar(request):
    if request.GET['comision']:
        cursos=Equipo.objects.filter(comision=request.GET['comision']) #trae de la BD los cursos que tenga la comision que se metió en la busqueda
        return render(request, "AppProyecto/resultado_busqueda.html", {'cursos':cursos})
    else:
        return render(request, "AppProyecto/busqueda_comision.html", {'mensaje':"No se ingresó una comision"} )


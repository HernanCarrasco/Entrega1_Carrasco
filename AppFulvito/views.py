from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar, Curso
from AppFulvito.forms import * 

lista=[]

def mostrar_fam(request):
    dict_cont={'lista':lista}
    return render (request, 'AppProyecto/Familia.html', dict_cont)


def crear_fam1(request):
    pariente1=Familiar(nombre="Lesbia", fecha_nacimiento="1952-5-31", edad=69, parentesco="Madre")
    pariente1.save()
    lista.append(pariente1)
    msg=f"Familiar creado: Nombre: {pariente1.nombre} Fecha de Nacimiento: {pariente1.fecha_nacimiento} Edad: {pariente1.edad} Parentesco: {pariente1.parentesco}"
    return HttpResponse(msg)

def crear_fam2(request):
    pariente2=Familiar(nombre="Hernan V.", fecha_nacimiento="1947-8-13", edad=75, parentesco="Padre")
    pariente2.save()
    lista.append(pariente2)
    msg=f"Familiar creado: Nombre: {pariente2.nombre} Fecha de Nacimiento: {pariente2.fecha_nacimiento} Edad: {pariente2.edad} Parentesco: {pariente2.parentesco}"
    return HttpResponse(msg)

def crear_fam3(request):
    pariente3=Familiar(nombre="Marian", fecha_nacimiento="1952-8-26", edad=29, parentesco="Hermana")
    pariente3.save()
    lista.append(pariente3)
    msg=f"Familiar creado: Nombre: {pariente3.nombre} Fecha de Nacimiento: {pariente3.fecha_nacimiento} Edad: {pariente3.edad} Parentesco: {pariente3.parentesco}"
    return HttpResponse(msg)


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

        formulario_user = CursoForm(request.POST)

        if formulario_user.is_valid():
            info=formulario_user.cleaned_data
            nombredelcurso=info["nombre"]
            comisiondelcurso=info["comision"]
            curso=Curso(nombre=nombredelcurso, comision=comisiondelcurso)
            curso.save()
            return render (request, "AppProyecto/inicio.html", {'mensaje': "Curso Creado!"})
    else:
        formulario_user=CursoForm()
        return render (request, "AppProyecto/crear_curso.html", {"formulario":formulario_user})

def busqueda_comision(request):
    return render (request, "AppProyecto/busqueda_comision.html")
    
def buscar(request):
    if request.GET['comision']:
        cursos=Curso.objects.filter(comision=request.GET['comision']) #trae de la BD los cursos que tenga la comision que se metió en la busqueda
        return render(request, "AppProyecto/resultado_busqueda.html", {'cursos':cursos})
    else:
        return render(request, "AppProyecto/busqueda_comision.html", {'mensaje':"No se ingresó una comision"} )


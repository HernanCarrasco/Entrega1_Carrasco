from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppFulvito.forms import * 


def inicio(request):
    return render (request, "AppFulvito/inicio.html")

def crear_reg(request):
    return render (request, "AppFulvito/crear_reg.html")


def crear_equipo(request):

    if request.method == "POST":

        formulario_user = EquipoForm(request.POST)

        if formulario_user.is_valid():
            info=formulario_user.cleaned_data
            nombre=info["nombre"]
            pais=info["pais"]
            año=info["año_fundacion"]
            titulos=info["nro_titulos"]
            equipo=Equipo(nombre=nombre, pais=pais, año_fundacion=año, nro_titulos=titulos)
            equipo.save()
            return render (request, "AppFulvito/inicio.html", {'mensaje': "Equipo Creado!"})
        else:
            return render (request, "AppFulvito/crear_equipo.html", {"formulario":formulario_user, 'mensaje': "Error en los datos"}) 
    else:
        formulario_user=EquipoForm()
        return render (request, "AppFulvito/crear_equipo.html", {"formulario":formulario_user})


def equipos(request):
    equipos=Equipo.objects.all() 
    return render(request, "AppFulvito/equipos.html", {'equipos':equipos})

def crear_jugador(request):

    if request.method == "POST":

        formulario_user = JugadorForm(request.POST)

        if formulario_user.is_valid():
            info=formulario_user.cleaned_data
            nombre=info["nombre"]
            edad=info["edad"]
            pais=info["pais"]
            equipo_jug=info["equipo"]
            jugador=Jugador(nombre=nombre, pais=pais, edad=edad, equipo=equipo_jug)
            jugador.save()
            return render (request, "AppFulvito/inicio.html", {'mensaje': "Jugador Creado!"})
        else:
            return render (request, "AppFulvito/crear_jugador.html", {"formulario":formulario_user, 'mensaje': "Error en los datos"}) 
    else:
        formulario_user=JugadorForm()
        return render (request, "AppFulvito/crear_jugador.html", {"formulario":formulario_user})

def jugadores(request):
    jugadores=Jugador.objects.all() 
    return render(request, "AppFulvito/jugadores.html", {'jugadores':jugadores})

def crear_entrenador(request):

    if request.method == "POST":

        formulario_user = EntrenadorForm(request.POST)

        if formulario_user.is_valid():
            info=formulario_user.cleaned_data
            nombre=info["nombre"]
            edad=info["edad"]
            pais=info["pais"]
            equipo_ent=info["equipo"]
            entrenador=Entrenador(nombre=nombre, pais=pais, edad=edad, equipo=equipo_ent)
            entrenador.save()
            return render (request, "AppFulvito/inicio.html", {'mensaje': "Entrenador Creado!"})
        else:
            return render (request, "AppFulvito/crear_entrenador.html", {"formulario":formulario_user, 'mensaje': "Error en los datos"}) 
    else:
        formulario_user=JugadorForm()
        return render (request, "AppFulvito/crear_entrenador.html", {"formulario":formulario_user})


def entrenadores(request):
    entrenadores=Entrenador.objects.all() 
    return render(request, "AppFulvito/entrenadores.html", {'entrenadores':entrenadores})


def crear_liga(request):

    if request.method == "POST":

        formulario_user = LigaForm(request.POST)

        if formulario_user.is_valid():
            info=formulario_user.cleaned_data
            nombre=info["nombre"]
            pais=info["pais"]
            liga=Liga(nombre=nombre, pais=pais)
            liga.save()
            return render (request, "AppFulvito/inicio.html", {'mensaje': "Liga Creada!"})
        else:
            return render (request, "AppFulvito/crear_liga.html", {"formulario":formulario_user, 'mensaje': "Error en los datos"}) 
    else:
        formulario_user=LigaForm()
        return render (request, "AppFulvito/crear_liga.html", {"formulario":formulario_user})

def ligas(request):
    ligas=Liga.objects.all() 
    return render(request, "AppFulvito/ligas.html", {'ligas':ligas})

def crear_campeonato(request):

    if request.method == "POST":

        formulario_user = CampeonatoForm(request.POST)

        if formulario_user.is_valid():
            info=formulario_user.cleaned_data
            nombre=info["nombre"]
            formato=info["formato"]
            nro_equipos=info["nro_equipos"]
            campeonato=Campeonato(nombre=nombre, formato=formato, nro_equipos=nro_equipos)
            campeonato.save()
            return render (request, "AppFulvito/inicio.html", {'mensaje': "Campeonato Creado!"})
        else:
            return render (request, "AppFulvito/crear_campeonato.html", {"formulario":formulario_user, 'mensaje': "Error en los datos"}) 
    else:
        formulario_user=JugadorForm()
        return render (request, "AppFulvito/crear_campeonato.html", {"formulario":formulario_user})

def campeonatos(request):
    campeonatos=Campeonato.objects.all() 
    return render(request, "AppFulvito/campeonatos.html", {'campeonatos':campeonatos})



def buscar(request):
    return render (request, "AppFulvito/buscar.html")

def busqueda(request):
    return render(request, "AppFulvito/busqueda.html" )

def busqueda2(request):
    return render(request, "AppFulvito/busqueda2.html" )

def busqueda3(request):
    return render(request, "AppFulvito/busqueda3.html" )
    
def busqueda_nombre(request):
    if request.GET['nombre']:
        jugadores=[Equipo.objects.filter(nombre__icontains=request.GET['nombre']), 
        Jugador.objects.filter(nombre__icontains=request.GET['nombre']),
        Entrenador.objects.filter(nombre__icontains=request.GET['nombre']),
        Liga.objects.filter(nombre__icontains=request.GET['nombre']),
        Campeonato.objects.filter(nombre__icontains=request.GET['nombre'])]               
        return render(request, "AppFulvito/resultado_busqueda.html", {'objeto1':jugadores[0], 
        'objeto2':jugadores[1],
        'objeto3':jugadores[2], 
        'objeto4':jugadores[3],
        'objeto5':jugadores[4],
        'busqueda':"nombres"})
    else:
        return render(request, "AppFulvito/buscar.html", {'mensaje':"No se ingresó un nombre para la busqueda."})



def busqueda_pais(request):
    if request.GET['pais']:
        jugadores=[Equipo.objects.filter(pais__icontains=request.GET['pais']), 
        Jugador.objects.filter(pais__icontains=request.GET['pais']),
        Entrenador.objects.filter(pais__icontains=request.GET['pais']),
        Liga.objects.filter(pais__icontains=request.GET['pais'])]               
        return render(request, "AppFulvito/resultado_busqueda.html", {'objeto1':jugadores[0], 
        'objeto2':jugadores[1],
        'objeto3':jugadores[2], 
        'objeto4':jugadores[3],
        'busqueda':"pais"})
    else:
        return render(request, "AppFulvito/buscar.html", {'mensaje':"No se ingresó un pais para la busqueda."})

def busqueda_equipo(request):
    if request.GET['equipo']:
        jugadores=[Jugador.objects.filter(equipo__icontains=request.GET['equipo']),
        Entrenador.objects.filter(equipo__icontains=request.GET['equipo'])]               
        return render(request, "AppFulvito/resultado_busqueda.html", {'objeto2':jugadores[0], 
        'objeto3':jugadores[1],
        'busqueda':"equipos"})
    else:
        return render(request, "AppFulvito/buscar.html", {'mensaje':"No se ingresó un equipo para la busqueda."} )


    


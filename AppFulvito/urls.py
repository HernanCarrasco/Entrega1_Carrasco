from django.urls import path    
from AppFulvito.views import *

urlpatterns = [
    
    path("", inicio, name="inicio"),
    path("crear_reg/", crear_reg, name="crear_reg"),
    path("crear_equipo/", crear_equipo, name="crear_equipo"),
    path("equipos/", equipos, name="equipos"),
    path("crear_jugador/", crear_jugador, name="crear_jugador"),
    path("jugadores", jugadores, name="jugadores"),
    path("crear_entrenador/", crear_entrenador, name="crear_entrenador"),
    path("entrenadores/", entrenadores, name="entrenadores"),
    path("crear_liga/", crear_liga, name="crear_liga"),
    path("ligas/", ligas, name="ligas"),
    path("crear_campeonato/", crear_campeonato, name="crear_campeonato"),
    path("campeonatos/", campeonatos, name="campeonatos"),
    path('buscar/', buscar, name="buscar"),
    path('busqueda/', busqueda, name="busqueda"),
    path('busqueda2/', busqueda2, name="busqueda2"),
    path('busqueda3/', busqueda3, name="busqueda3"),
    path('busqueda_nombre/', busqueda_nombre, name="busqueda_nombre"),
    path('busqueda_pais/', busqueda_pais, name="busqueda_pais"),
    path('busqueda_equipo/', busqueda_equipo, name="busqueda_equipo"),
    
    ]
from django.db import models

class Equipo(models.Model):
    nombre=models.CharField(max_length=40)
    año_fundacion=models.DateField()
    nro_titulos=models.IntegerField()
    pais=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    pais=models.CharField(max_length=20)
    equipo=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Entrenador(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    pais=models.CharField(max_length=20)
    equipo=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
        

class Liga(models.Model):
    nombre=models.CharField(max_length=50)
    pais=models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre

class Campeonato(models.Model):
    nombre=models.CharField(max_length=50)
    nro_equipos=models.IntegerField()
    formato=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

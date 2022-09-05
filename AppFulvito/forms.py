from django import forms


class Equipo(forms.Form):
    nombre=forms.CharField(max_length=40)
    año_fundacion=forms.DateField()
    nro_titulos=forms.IntegerField()
    pais=forms.CharField(max_length=20)


class Jugador(forms.Form):
    nombre=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    pais=forms.CharField(max_length=20)
    equipo=forms.CharField(max_length=50)


class Entrenador(forms.Form):
    nombre=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    pais=forms.CharField(max_length=20)
    equipo=forms.CharField(max_length=50)


class Liga(forms.Form):
    nombre=forms.CharField(max_length=50)
    pais=forms.CharField(max_length=20)

class Campeonato(forms.Form):
    nombre=forms.CharField(max_length=50)
    nro_equipos=forms.IntegerField()
    formato=forms.CharField(max_length=20)

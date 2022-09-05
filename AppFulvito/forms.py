from django import forms


class EquipoForm(forms.Form):
    nombre=forms.CharField(max_length=40)
    año_fundacion=forms.DateField()
    nro_titulos=forms.IntegerField()
    pais=forms.CharField(max_length=20)


class JugadorForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    pais=forms.CharField(max_length=20)
    equipo=forms.CharField(max_length=50)


class EntrenadorForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    pais=forms.CharField(max_length=20)
    equipo=forms.CharField(max_length=50)


class LigaForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    pais=forms.CharField(max_length=20)

class CampeonatoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    nro_equipos=forms.IntegerField()
    formato=forms.CharField(max_length=20)

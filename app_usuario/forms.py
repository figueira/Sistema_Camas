from django import forms
from models import *
from django.forms.widgets import CheckboxSelectMultiple


class IniciarSesionForm(forms.Form):
    unombre = forms.CharField(
                      max_length = 64,
                      widget = forms.TextInput(
                                 attrs = {
                                     'placeholder': 'Cedula de identidad:',
                                     'class': 'span2'
                                     }))
    uclave = forms.CharField(max_length = 32,
                             widget = forms.PasswordInput(attrs = {
                                 'placeholder':'Clave:',
                                 'class':'span2'
                                 }))


class SolicitarCuenta(forms.Form):
    cedula          = forms.IntegerField(widget=forms.TextInput)
    nombres         = forms.CharField()
    apellidos       = forms.CharField()
    tipo            = forms.ChoiceField(choices = USUARIO)
    email           = forms.EmailField(max_length = 64)
    email0          = forms.EmailField(max_length = 64)
    clave           = forms.CharField(widget = forms.PasswordInput())
    clave0          = forms.CharField(widget = forms.PasswordInput())
    administrador   = forms.BooleanField(required = False)

#class cambioClave(forms.Form):
    #claveV = forms.CharField(widget = forms.PasswordInput())
    #clave = forms.CharField(widget = forms.PasswordInput())
    #claveO = forms.CharField(widget = forms.PasswordInput())

#class restablecerClave(forms.Form):
    #correo = forms.EmailField(max_length = 64)
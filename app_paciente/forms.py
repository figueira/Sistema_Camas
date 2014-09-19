from django import forms
from models import *

class agregar_paciente_form(forms.Form):
    num_historia     = forms.IntegerField(
                            max_value=999999,
                            widget = forms.TextInput(attrs={'size': 6}))
    tipo_cedula      = forms.ChoiceField(
                            choices=TIPO_CEDULA,
                            widget=forms.RadioSelect())
    cedula           = forms.IntegerField(max_value=999999999)
    nombres          = forms.CharField(max_length=64)
    apellidos        = forms.CharField(max_length=64)
    sexo             = forms.ChoiceField(choices=SEXO)
    
    fecha_nacimiento          = forms.DateField(
                        label = "FECHA DE NACIMIENTO",
                        widget = forms.TextInput(attrs = {
                            'placeholder':'dd/mm/aaaa',
                            'data-format':'dd/mm/yyyy'
                            }))
    fecha_ingreso_institucion = forms.DateField(
                        label = "FECHA DE INGRESO A LA INSTITUCION",
                        widget = forms.TextInput(attrs = {
                            'placeholder':'dd/mm/aaaa',
                            'data-format':'dd/mm/yyyy'
                            }))
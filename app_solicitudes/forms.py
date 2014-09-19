from django import forms
from models import *
from app_usuario.lookups import MedicoLookup
from django.forms.widgets import CheckboxSelectMultiple
from django.utils.safestring import mark_safe, SafeData

from selectable.forms import AutoCompleteWidget

class SolicitarHabitacion(forms.Form):
    cedula          = forms.IntegerField(widget = forms.TextInput)
    diagnostico     = forms.CharField(max_length = 64)
    codigo_doctor   = forms.CharField(
                        label='Doctor',
                        widget = AutoCompleteWidget(MedicoLookup),
                        required=False,
    )
    fecha_ingreso = forms.DateField(
                        label = "FECHA ESTIMADA DE INGRESO",
                        widget = forms.TextInput(attrs = {
                            'placeholder':'dd/mm/aaaa',
                            }))
    fecha_salida = forms.DateField(
                        label = "FECHA ESTIMADA DE SALIDA",
                        widget = forms.TextInput(attrs = {
                            'placeholder':'dd/mm/aaaa',
                            }))
    procedencia = forms.ChoiceField(choices = PROCEDENCIA)
    correo_solicitante = forms.EmailField()
    observacion = forms.CharField(max_length = 140, required = False)
    
    
class SolicitarPacienteNuevo(forms.Form):
    num_historia     = forms.IntegerField(
                            max_value=999999,
                            widget = forms.TextInput(attrs={'size': 6}))
    tipo_cedula      = forms.ChoiceField(
                            choices=TIPO_CEDULA,
                            widget=forms.RadioSelect())
    cedula           = forms.IntegerField(
                            max_value=999999999,
                            widget = forms.TextInput(attrs={'size': 9}))
    nombres          = forms.CharField(max_length=64)
    apellidos        = forms.CharField(max_length=64)
    sexo             = forms.ChoiceField(choices=SEXO)
    
    fecha_nacimiento = forms.DateField(
                        label = "FECHA DE NACIMIENTO",
                        widget = forms.TextInput(attrs = {
                            'placeholder':'dd/mm/aaaa',
                            'data-format':'dd/mm/yyyy'
                            }))
    diagnostico     = forms.CharField(max_length = 64)
    codigo_doctor   = forms.CharField(
                        label='Doctor',
                        widget = AutoCompleteWidget(MedicoLookup),
                        required=False,
    )
    fecha_ingreso = forms.DateField(
                        label = "FECHA ESTIMADA DE INGRESO",
                        widget = forms.TextInput(attrs = {
                            'placeholder':'dd/mm/aaaa',
                            }))
    fecha_salida = forms.DateField(
                        label = "FECHA ESTIMADA DE SALIDA",
                        widget = forms.TextInput(attrs = {
                            'placeholder':'dd/mm/aaaa',
                            }))
    procedencia = forms.ChoiceField(choices = PROCEDENCIA)
    correo_solicitante = forms.EmailField()
    observacion = forms.CharField(max_length = 140, required = False)
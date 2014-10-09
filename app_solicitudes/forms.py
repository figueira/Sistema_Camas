from django import forms
from models import *
from app_usuario.lookups import MedicoLookup
from django.forms.widgets import CheckboxSelectMultiple
from django.utils.safestring import mark_safe, SafeData

from selectable.forms import AutoCompleteWidget

class SolicitarHabitacion(forms.Form):
    cedula          = forms.IntegerField(
                        widget = forms.TextInput(
                            attrs = {
                                'placeholder': 'Cedula de identidad del Paciente',
                                'class': 'form-control'
                            }
                        )
                    )
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
                            widget = forms.TextInput(
                                attrs={
                                    'size': 6,
                                    'class': 'form-control',
                                    'placeholder':'Numero de Historia'
                                }
                            )
                        )
    tipo_cedula      = forms.ChoiceField(
                            choices=TIPO_CEDULA,
                            widget=forms.Select(
                            )
                        )

    cedula           = forms.IntegerField(
                            max_value=999999999,
                            widget = forms.TextInput(
                                attrs={
                                    'size': 9,
                                    'class': 'form-control',
                                    'placeholder':'Cedula de identidad'
                                }
                            )
                        )
    nombres          = forms.CharField(
                            max_length=64,
                            widget = forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder':'Nombre'
                                }
                            )
                         )
    apellidos        = forms.CharField(
                            max_length=64,
                            widget = forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder':'Apellido'
                                }
                            )
                        )
    sexo             = forms.ChoiceField(
                            choices=SEXO,
                            widget=forms.Select(
                                attrs={
                                    'class':'form-control'
                                }
                            )
                        )
    
    fecha_nacimiento = forms.DateField(
                            label = "FECHA DE NACIMIENTO",
                            widget = forms.TextInput(
                                attrs = {
                                    'placeholder':'dd/mm/aaaa',
                                    'data-format':'dd/mm/yyyy',
                                    'class': 'form-control'
                                }
                            )
                        )
    diagnostico   = forms.CharField(
                        max_length = 64, 
                        widget = forms.Textarea(
                            attrs={
                                'class': 'form-control textarea',
                                'placeholder':'Diagnostico'
                            }
                        )
                    )

    codigo_doctor = forms.CharField(
                        label='Doctor',
                        widget = AutoCompleteWidget(
                            MedicoLookup, 
                            attrs = {
                                'placeholder':'Codigo del Doctor',
                                'class': 'form-control',
                            }
                        ),
                        required=False,
                    )

    fecha_ingreso = forms.DateField(
                        label = "FECHA ESTIMADA DE INGRESO",
                        widget = forms.TextInput(
                            attrs = {
                                'placeholder':'Fecha de ingreso (dd/mm/aaaa)',
                                'class': 'form-control',
                            }
                        )
                    )

    fecha_salida =  forms.DateField(
                        label = "FECHA ESTIMADA DE SALIDA",
                        widget = forms.TextInput(
                            attrs = {
                                'placeholder':'Fecha de salida (dd/mm/aaaa)',
                                'class' : 'form-control'
                            }
                        )
                    )

    procedencia =   forms.ChoiceField(
                        choices = PROCEDENCIA,
                        widget=forms.Select(
                            attrs={
                                'class':'form-control'
                            }
                        )
                    )


    correo_solicitante = forms.EmailField(
                        widget=forms.EmailInput(
                            attrs = {
                                'placeholder': 'Email del Solicitante',
                                'class': 'form-control'
                            }
                        )
                    )
    observacion   = forms.CharField(
                        max_length = 140, 
                        required = False,
                        widget=forms.Textarea(
                            attrs = {
                                'placeholder': 'Observaciones',
                                'class': 'form-control textarea'
                            }
                        )
                    )
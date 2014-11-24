from django import forms
from models import *
from app_usuario.lookups import MedicoLookup
from django.forms.widgets import CheckboxSelectMultiple
from django.utils.safestring import mark_safe, SafeData

from selectable.forms import AutoCompleteWidget

class BaseSolicitar(forms.Form):

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
								'style' : 'border: 1px solid #ccc;',
							}
						),
						required=False,
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


class SolicitarHabitacion(BaseSolicitar):
	fecha_ingreso2 = forms.DateField(
						label = "FECHA-INGRESO-2",
						widget = forms.TextInput(
							attrs = {
								'placeholder':'Fecha de ingreso (dd/mm/aaaa)',
								'class': 'form-control',
							}
						)
					)
	fecha_salida2 =  forms.DateField(
						label = "FECHA-SALIDA-2",
						widget = forms.TextInput(
							attrs = {
								'placeholder':'Fecha de salida (dd/mm/aaaa)',
								'class' : 'form-control'
							}
						)
					)
	
	
class SolicitarPacienteNuevo(BaseSolicitar):
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
							label = "FECHA-NACIMIENTO",
							widget = forms.TextInput(
								attrs = {
									'placeholder':'Fecha de Nacimiento (dd/mm/aaaa)',
									'data-format':'dd/mm/yyyy',
									'class': 'form-control'
								}
							)
						)
	fecha_ingreso = forms.DateField(
						label = "FECHA-INGRESO",
						widget = forms.TextInput(
							attrs = {
								'placeholder':'Fecha de ingreso (dd/mm/aaaa)',
								'class': 'form-control',
							}
						)
					)
	fecha_salida =  forms.DateField(
						label = "FECHA-SALIDA",
						widget = forms.TextInput(
							attrs = {
								'placeholder':'Fecha de salida (dd/mm/aaaa)',
								'class' : 'form-control'
							}
						)
					)

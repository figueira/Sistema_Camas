from django import forms
from models import *

class HabitacionForm(forms.Form):
	
	numero_habitacion = forms.IntegerField(
								widget = forms.TextInput(
									attrs={
										'readonly':'readonly',
									}
								))

	numero_historia = forms.IntegerField(
								widget = forms.TextInput(
									attrs={
										'readonly':'readonly', 
										'class': 'form-control',
										'style': 'background : white; cursor: auto;'
									}
								))

	nombre = forms.CharField(
								max_length = 64,
								widget = forms.TextInput(
									attrs={
										'readonly':'readonly', 
										'class': 'form-control',
										'style': 'background : white; cursor: auto;'
									}
								))

	nombre_medico = forms.CharField(
								max_length = 64,
								widget = forms.TextInput(
									attrs={
										'readonly':'readonly', 
										'class': 'form-control',
										'style': 'background : white; cursor: auto;'
									}
								))

	fecha = forms.CharField(
								widget = forms.TextInput(
									attrs={
										'readonly':'readonly', 
										'class': 'form-control',
										'style': 'background : white; cursor: auto;'
									}
								))

	procedencia = forms.CharField(
								widget = forms.TextInput(
									attrs={
										'readonly':'readonly', 
										'class': 'form-control',
										'style': 'background : white; cursor: auto;'
									}
								))
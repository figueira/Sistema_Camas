from django import forms
from models import *
from django.forms.widgets import CheckboxSelectMultiple


class IniciarSesionForm(forms.Form):
	unombre = forms.CharField(
					  max_length = 64,
					  widget = forms.TextInput(
								 attrs = {
									 'placeholder': 'Cedula de identidad:',
									 'class': 'form-control'
									 }))
	uclave = forms.CharField(max_length = 32,
							 widget = forms.PasswordInput(attrs = {
								 'placeholder':'Clave:',
								 'class':'form-control'
								 }))


class BaseUserForm(forms.Form):
	cedula          = forms.IntegerField(
						widget=forms.NumberInput(
							attrs = {
								'placeholder': 'Cedula de identidad',
								'class': 'form-control'
							}
						)
					)
	nombres         = forms.CharField(
						widget=forms.TextInput(
							attrs = {
								'placeholder': 'Nombre',
								'class': 'form-control'
							}
						)
					)
	apellidos       = forms.CharField(
						widget=forms.TextInput(
							attrs = {
								'placeholder': 'Apellido',
								'class': 'form-control'
							}
						)
					)
	tipo            = forms.ChoiceField(
						choices = USUARIO,
						widget=forms.Select(
							attrs={
								'class':'form-control'
							}
						)
					)
	email           = forms.EmailField(
						max_length = 64,
						widget=forms.EmailInput(
							attrs = {
								'placeholder': 'Email',
								'class': 'form-control'
							}
						)
					)
	email0          = forms.EmailField(
						max_length = 64,
						widget=forms.EmailInput(
							attrs = {
								'placeholder': 'Confirmacion de Email',
								'class': 'form-control'
							}
						)
					)
	administrador   = forms.BooleanField(required = False)


class SolicitarCuenta(BaseUserForm):
	
	clave           = forms.CharField(
						widget = forms.PasswordInput(
							attrs = {
								'placeholder': 'Clave',
								'class': 'form-control'
							}
						)
					)
	clave0          = forms.CharField(
						widget = forms.PasswordInput(
							attrs = {
								'placeholder': 'Confirmacion de Clave',
								'class': 'form-control'
							}
						)
					)
	

class EditarCuenta(BaseUserForm):
	clave           = forms.CharField(
						required = False,
						widget = forms.PasswordInput(
							attrs = {
								'placeholder': 'Clave Actual',
								'class': 'form-control'
							}
						)
					)
	claveNueva          = forms.CharField(
						required = False,
						widget = forms.PasswordInput(
							attrs = {
								'placeholder': 'Nueva Clave',
								'class': 'form-control'
							}
						)
					)
	claveNueva0	= forms.CharField(
						required = False,
						widget = forms.PasswordInput(
							attrs = {
								'placeholder': 'Confirmacion de Nueva Clave',
								'class': 'form-control'
							}
						)
					)
	cambiarClave   = forms.BooleanField(
						required = False,
						widget = forms.CheckboxInput(
							attrs = {
								'id': 'cambiar_clave_checkbox',
							}
						)
					)


class restablecerClave(forms.Form):
	
	usuario          = forms.IntegerField(
						widget=forms.NumberInput(
							attrs = {
								'placeholder': 'Cedula de identidad',
								'class': 'form-control'
							}
						)
					)        
	correo           = forms.EmailField(
						max_length = 64,
						widget=forms.EmailInput(
							attrs = {
								'placeholder': 'Email',
								'class': 'form-control'
							}
						)
					)  
#class cambioClave(forms.Form):
	#claveV = forms.CharField(widget = forms.PasswordInput())
	#clave = forms.CharField(widget = forms.PasswordInput())
	#claveO = forms.CharField(widget = forms.PasswordInput())

#class restablecerClave(forms.Form):
	#correo = forms.EmailField(max_length = 64)

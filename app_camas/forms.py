from django import forms
from models import *

class HabitacionForm(forms.Form):
	
	numero_habitacion = forms.IntegerField(
                        widget = forms.TextInput(attrs={'readonly':'readonly'}))
	numero_historia = forms.IntegerField(
                      widget = forms.TextInput(attrs={'readonly':'readonly'}))
	nombre = forms.CharField(max_length = 64,
             widget = forms.TextInput(attrs={'readonly':'readonly'}))
	nombre_medico = forms.CharField(max_length = 64,
                    widget = forms.TextInput(attrs={'readonly':'readonly'}))
	fecha = forms.CharField(
            widget = forms.TextInput(attrs={'readonly':'readonly'}))
	procedencia = forms.CharField(
                  widget = forms.TextInput(attrs={'readonly':'readonly'}))
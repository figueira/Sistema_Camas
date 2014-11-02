from django.core.exceptions import ObjectDoesNotExist

##from django.shortcuts import render
# Manejo de Sesion
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Formularios
from django.core.context_processors import csrf
from django.template import RequestContext
from django.forms.widgets import CheckboxSelectMultiple

# General HTML
from django.shortcuts import render_to_response,redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.forms.formsets import formset_factory

# Manejo de Informacion de esta aplicacion
from models import *
from forms import *
from app_usuario.models import *

from datetime import date
from django.utils import simplejson
from django.core import serializers
import pdb
from django.contrib import messages

# Cantidad de segundos en 1,2,..,6 horas
# hora_en_segundos[0] -> Segundos en 0 horas
# hora_en_segundos[1] -> Segundos en 1 hora
# .
# .
# .
# hora_en_segundos[6] -> Segundos en 6 horas
hora_en_segundos = [0,3600,7200,10800,14400,18000,21600] 

def buscar_paciente_cedula(request):
	if request.method == 'POST':
		c = request.POST['cedula']
		paciente = serializers.serialize('json', Paciente.objects.filter(cedula = c))
		hay = Paciente.objects.filter(cedula = c)
		if hay:
			data = {
				'result' : 'success',
				'message' : paciente,
			}
		else:
			data = {
				'result' : 'error',
				'message' : 'La cedula ingresada no se encuentra en el sistema.',
			}
		return HttpResponse(simplejson.dumps(data), content_type='application/json')

@login_required(login_url='/')
def solicitar_habitacion(request):
    mensaje = ""
    msj_tipo = ""
    msj_info = ""
    mnj_fecha = ""
    
    if request.method == 'POST':
            
        form = SolicitarHabitacion(request.POST)
        if form.is_valid():            
            pcd = form.cleaned_data
            s_cedula                = pcd['cedula']
            s_diagnostico           = pcd['diagnostico']
            s_codigo_doctor         = pcd['codigo_doctor']
            s_fecha_ingreso         = pcd['fecha_ingreso']
            s_fecha_salida          = pcd['fecha_salida']
            s_procedencia           = pcd['procedencia']
            s_correo_solicitante    = pcd['correo_solicitante']
            s_observacion           = pcd['observacion']
                        
            try:
                newPaciente = Paciente.objects.get(cedula = s_cedula)
                try:
                    newMedico = Medico.objects.get( codigo = s_codigo_doctor )
                                        
                    if (s_fecha_ingreso <= s_fecha_salida):
                        s = Solicitud(paciente = newPaciente,
                                medico = newMedico,
                                diagnostico = s_diagnostico,
                                fecha_ingreso = s_fecha_ingreso,
                                fecha_salida = s_fecha_salida,
                                procedencia = s_procedencia,
                                correo_solicitante = s_correo_solicitante,
                                observacion = s_observacion)
                        s.save()
                        
                        messages.success(request, 'La solicitud fue enviada con exito')
                        return redirect('/')
                    else:
                        mnj_fecha = "La fecha de ingreso debe ser menor que la de egreso."
                except ObjectDoesNotExist:
                    msj_tipo = "error"
                    msj_info = "El medico no se encuentra registrado en el sistema."
            except ObjectDoesNotExist:
                msj_tipo = "error"
                msj_info = "El paciente no se encuentra registrado en el sistema."
            except:
                msj_tipo = "error"
                msj_info = "Ya existe una solicitud con este paciente."
        
        form2 = SolicitarPacienteNuevo()
        info = {
            'msj_tipo':msj_tipo,
            'msj_info':msj_info,
            'form':form, 
            'form2':form2, 
            'mnj_fecha':mnj_fecha
            }
        return render_to_response('solicitar_habitacion.html',info,context_instance=RequestContext(request))
    form = SolicitarHabitacion()
    form2 = SolicitarPacienteNuevo()
    info = {
        'form':form,
        'form2':form2
        }
    return render_to_response('solicitar_habitacion.html',info,context_instance=RequestContext(request))


@login_required(login_url='/')
def solicitar_paciente_nuevo(request):
    mensaje = ""
    msj_tipo = ""
    msj_info = ""
    mnj_fecha = ""
    
    form = SolicitarPacienteNuevo(request.POST)
    if form.is_valid():
        pcd = form.cleaned_data
        s_num_historia          = pcd['num_historia']
        s_tipo_cedula           = pcd['tipo_cedula']
        s_cedula                = pcd['cedula']
        s_nombres               = pcd['nombres']
        s_apellidos             = pcd['apellidos']
        s_sexo                  = pcd['sexo']
        s_fecha_nacimiento      = pcd['fecha_nacimiento']
        s_diagnostico			= pcd['diagnostico']
        s_codigo_doctor			= pcd['codigo_doctor']
        s_fecha_ingreso			= pcd['fecha_ingreso']
        s_fecha_salida			= pcd['fecha_salida']
        s_procedencia			= pcd['procedencia']
        s_correo_solicitante	= pcd['correo_solicitante']
        s_observacion			= pcd['observacion']

        try:
            newPaciente = Paciente.objects.get(cedula = s_cedula)
        except ObjectDoesNotExist:
            p = Paciente(
                    num_historia = s_num_historia,
                    tipo_cedula = s_tipo_cedula,
                    cedula = s_cedula,
                    nombres = s_nombres,
                    apellidos = s_apellidos,
                    sexo = s_sexo,
                    fecha_nacimiento = s_fecha_nacimiento,
                    fecha_ingreso_institucion = date.today()
                )
            p.save()
            newPaciente = Paciente.objects.get(cedula = s_cedula)
            print newPaciente
            try:
                newMedico = Medico.objects.get( codigo = s_codigo_doctor )
                                    
                if (s_fecha_ingreso <= s_fecha_salida):
                    s = Solicitud(
                            paciente = newPaciente,
                            medico = newMedico,
                            diagnostico = s_diagnostico,
                            fecha_ingreso = s_fecha_ingreso,
                            fecha_salida = s_fecha_salida,
                            procedencia = s_procedencia,
                            correo_solicitante = s_correo_solicitante,
                            observacion = s_observacion
                        )
                    s.save()
                    
                    messages.success(request, 'La solicitud fue enviada con exito')
                    return redirect('/')
                else:
                    mnj_fecha = "La fecha de ingreso debe ser menor que la de egreso."
            except ObjectDoesNotExist:
                msj_tipo = "error"
                msj_info = "El medico no se encuentra registrado en el sistema."
        except:
            msj_tipo = "error"
            msj_info = "Ya existe una solicitud con este paciente."
    
    f = SolicitarHabitacion()
    info = {
        'msj_tipo':msj_tipo,
        'msj_info':msj_info,
        'form':f,
        'form2':form, 
        'mnj_fecha':mnj_fecha
        }
    return render_to_response('solicitar_habitacion.html',info,context_instance=RequestContext(request))


@login_required(login_url='/')	
def lista_solicitudes(request):
    
    solicitudes_activas = Solicitud.objects.all().filter(activa=True).order_by('fecha_ingreso')
    
    info = {
    'solicitudes_activas':solicitudes_activas}
    return render_to_response('lista_solicitudes.html',info,context_instance=RequestContext(request))
    
    
@login_required(login_url='/')
def cancelar_solicitud(request):
    if request.method == 'POST':
        #pdb.set_trace()
        c = request.POST['id']
        identificador = Solicitud.objects.filter(id=c)
        if identificador:
            Solicitud.objects.filter(id=c).delete()
            data = {
                'result' : 'success',
            }
        else:
            data = {
                'result' : 'error',
            }
    return HttpResponse(simplejson.dumps(data), content_type='application/json')
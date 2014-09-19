from django.shortcuts import render
# Manejo de Sesion
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# General HTML
from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from app_solicitudes.models import *
from app_camas.models import *
from app_estadisticas.models import *

from datetime import *
from django.utils import timezone
from time import mktime,strptime
import pdb

from django.utils import simplejson
from simple_history.models import HistoricalRecords

# Termometro = {'fecha':camas}
camas_libres = Habitacion.objects.all().filter(estado='D')
camas_verdes = []
camas_amarillas = Ingreso.objects.all().filter(habitacion__estado='O') 
camas_rojas = []
camas = [camas_libres, camas_verdes, camas_amarillas, camas_rojas]
Termometro = {'2014-06-08':camas}

# Te da la fecha del dia de la semana mas cercano hacia atras.
def dia_anterior(d, weekday):
	days_back = d.weekday() - weekday
	if days_back <= 0:
		return d + timedelta(-days_back)
	
	return d - timedelta(days_back)
	
# Te dice si la habitacion ha estado
# - libre
# - ocupada por menos de 3 dias
# - ocupada entre 3 y 4
# - ocupada 5 o mas dias
def dias_ocupada( hab , dia ):
	
	historia = hab.history.as_of(dia)
	
	# Si en la historia de hoy esta libre, esta libre :D
	if historia.estado == 'D':
		return 0
	# Si esta en mantenimiento retorno mas de 5 dias
	elif historia.estado == 'M':
		return 5
	# Si no, esta ocupada en proceso de alta o en proceso de limpieza
	else:
		num_dias = 5
		dias_ocupada = 1 # Ya se que al menos lleva un dia ocupada
		for d in range(1,num_dias):
			
			try:
				historia2 = hab.history.as_of(dia-timedelta(d))
			except:
				return dias_ocupada # Si no existia historia, estaba libre este dia
			
			if historia2.estado == 'D':
				return dias_ocupada # Si estaba libre este dia, cuento cuantos dias estuvo ocupada
				
			dias_ocupada+=1 # Sigo sumando dias
			
		return 5 # Si nunca sali del for, llevo mas de 5 dias

@login_required(login_url='/')
def termometro(request , dia = None , mes = None , ano = None ):
	
	habs = Habitacion.objects.all().order_by('numero')
	termometros_semana = []
	hoy = datetime.now()
	
	if dia and mes and ano:
		fecha = strptime('%s/%s/%s' % (dia,mes,ano),"%d/%m/%Y")
		fecha = datetime.fromtimestamp(mktime(fecha))
	else:
		fecha = datetime.now()

	for dia_numero in range(7):
		
		termometro = []
		dia = dia_anterior(fecha,dia_numero)
		
		if dia > hoy:
			termometros_semana.append({
				'dia' : dia,
				'habs': None,
			})
			continue
	
		for h in habs:
			try:
				h1 = h.history.as_of(dia)
				termometro.append({
					'hab':h1,
					'dias_ocu':dias_ocupada(h1,dia),
				})
			except:
				h.estado = 'D'
				termometro.append({
					'hab':h,
					'dias_ocu':0
				})
		
		termometro = sorted(termometro, key=lambda k: k['dias_ocu'])
				
		termometros_semana.append({
				'dia' : dia,
				'habs': termometro,
			})
	
	semana_ant = (fecha - timedelta(7)).strftime('%d/%m/%Y')
	semana_sig = (fecha + timedelta(7)).strftime('%d/%m/%Y')
	semana_act = datetime.now().strftime('%d/%m/%Y')
	
	info = {
		'termometros': termometros_semana,
		'semana_ant': semana_ant,
		'semana_act': semana_act,
		'semana_sig': semana_sig,
	}
	
	return render_to_response('estadistica_termometro.html',info,context_instance=RequestContext(request))

@login_required(login_url='/')
def matriz(request):

	hab_libre =	 [ item for item in Habitacion.objects.all().filter(estado='D') ]
	hab_alta = [ item for item in Habitacion.objects.all().filter(estado='A') ]
	hab_ocu = [ item for item in Habitacion.objects.all().filter(estado='O') ]
	hab_limp = [ item for item in Habitacion.objects.all().filter(estado='L') ]
	hab_mant = [ item for item in Habitacion.objects.all().filter(estado='M') ]
	
	habs = hab_libre + hab_alta + hab_ocu + hab_limp + hab_mant
	habs.sort( key = lambda x: x.numero , reverse = False )
	info = {}
	info['habs'] = habs
	info['hoy'] = timezone.now().date()
	
	return render_to_response('estadistica_matriz.html',info,context_instance=RequestContext(request))

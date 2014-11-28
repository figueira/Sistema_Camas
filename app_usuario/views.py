import json
import itertools

# -*- encoding: utf-8 -*-
# Manejo de Sesion
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Formularios
from django.core.context_processors import csrf
from django.core import serializers
from django.db.models import Q
from django.template import RequestContext
from django.forms.widgets import CheckboxSelectMultiple

# General HTML
from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest

# Manejo de Informacion de esta aplicacion
from forms import *
from models import *

# Envio de Correos
from django.core.mail import EmailMessage


def sesion_iniciar(request):
	
	if request.user.is_authenticated():
		info = {}
		if not request.user.is_staff:
			usuario = get_object_or_404(Usuario, username=request.user.username)
			info = {'usuario': usuario}
		return render_to_response('loged.html',info,context_instance=RequestContext(request))
	
	if request.method == 'POST':
		unombre = request.POST.get('unombre', 'userDefault')
		uclave  = request.POST.get('uclave', 'psswdDefault')
		user = authenticate(username=unombre, password=uclave)
		
		#Si le doy a iniciar sesion y NO estoy en el home, tengo userDefault y
		#psswdDefault, redirecciono al home para introducir datos
		if unombre == "userDefault" and uclave=="psswdDefault":
			msj_tipo = ""
			msj_info = ""
			form = IniciarSesionForm()
			info = {'msj_tipo':msj_tipo,'msj_info':msj_info,'form':form}
			return render_to_response('index.html',info,context_instance=RequestContext(request))

		if user is not None:
			if user.is_active:
				login(request,user)
				info = {}
				if not user.is_staff:
					usuario = get_object_or_404(Usuario,username=request.user.username)
					info = {'usuario':usuario}
				return render_to_response('loged.html',info,context_instance=RequestContext(request))

		msj_tipo = "danger"
		msj_info = "Error en clave"
		form = IniciarSesionForm()
		info = {'msj_tipo':msj_tipo,'msj_info':msj_info,'form':form}
		return render_to_response('index.html',info,context_instance=RequestContext(request))
	form = IniciarSesionForm()
	info = {'form':form}
	return render_to_response('index.html',info,context_instance=RequestContext(request))


def sesion_cerrar(request):
	logout(request)
	return redirect('/')


def clave_restablecer(request):
	mensaje = ""
	if request.method == 'POST':
		formRestablecer = restablecerClave(request.POST)
		if formRestablecer.is_valid():
			pcd = formRestablecer.cleaned_data
			f_correo = pcd['correo']
			f_usuario = pcd['usuario']
			usuario = Usuario.objects.filter(email=f_correo)
			if len(usuario) == 0 :
				mensaje = "Correo Invalido"
			else:
				usuario = Usuario.objects.get(username=f_usuario)
				clave = User.objects.make_random_password()
				email = EmailMessage('[GenSE] Admin - Cambio de Clave','Estimado/a '+usuario.first_name+' '+usuario.last_name+'\n\nSe recibio una solicitud de cambiar su clave, la nueva clave es: '+clave+'\n\nSaludos,\nAdministrador del Sistema', to=[f_correo]) 
				email.send()
				usuario.set_password(clave)
				usuario.save()

				msj_tipo = "success"
				mensaje = "Su nueva clave fue enviada al correo suministrado"
				formRestablecer = restablecerClave()
				form = IniciarSesionForm()
				info = {'formRestablecer':formRestablecer,'form':form,'msj_tipo':msj_tipo,'msj_info':mensaje}
				return render_to_response('restablecerClave.html',info,context_instance=RequestContext(request))
		else:
			msj_tipo = "danger"
			mensaje = "Existen errores con el formulario."
			formRestablecer = restablecerClave()
			form = IniciarSesionForm()
			info = {'formRestablecer':formRestablecer,'form':form,'msj_tipo':msj_tipo,'msj_info':mensaje}
			return render_to_response('restablecerClave.html',info,context_instance=RequestContext(request))

	formRestablecer = restablecerClave()
	form = IniciarSesionForm()
	info = {'form':form,'formRestablecer':formRestablecer}
	return render_to_response('restablecerClave.html',info,context_instance=RequestContext(request))


def usuario_crear(request):
	mensaje = ""
	if request.method == 'POST':
		form = SolicitarCuenta(request.POST)
		if form.is_valid():
			pcd = form.cleaned_data
			u_tipo		       = pcd['tipo']
			u_codigoMedico	   = pcd['codigoMedico']
			u_cedula           = pcd['cedula']
			u_nombres          = pcd['nombres']
			u_apellidos        = pcd['apellidos']
			u_email            = pcd['email']
			u_email0           = pcd['email0']
			u_clave            = pcd['clave']
			u_clave0           = pcd['clave0']
			u_administrador    = pcd['administrador']

			prueba = Usuario.objects.filter(username=u_cedula)
			prueba2 = (u_clave==u_clave0)

			if not prueba:
				if prueba2:
					prueba2 = (u_email==u_email0)
					if prueba2:

						if u_tipo == 'M' and u_codigoMedico == '':
							msj_info = "Para el tipo de usuario 'Medico' el campo 'Codigo del medico' es requerido."
						
						else :
							u = None
							if u_tipo != 'M' : 
								u = Usuario(
									username=u_cedula,
									first_name=u_nombres,
									last_name=u_apellidos,
									tipo=u_tipo,
									email=u_email,
									password=u_clave
								)
							elif u_tipo == 'M' and u_codigoMedico:
								u = Medico(
									username=u_cedula,
									first_name=u_nombres,
									last_name=u_apellidos,
									tipo=u_tipo,
									codigo=u_codigoMedico,
									email=u_email,
									password=u_clave
								)
							u.is_active = True
							u.set_password(u_clave)
							if u_administrador == True:
								u.is_staff = True
							u.save()
							return redirect('/usuario/listar')

					else:
						msj_info = "No hubo coincidencia con los emails ingresados."     
				else:
					msj_info = "No hubo coincidencia con las claves ingresadas."     
			else:
				msj_info = "Ya hay un usuario registrado con esa cedula." 
		else:
			msj_info = "Error con el formulario."

		msj_tipo = "danger"
		info = {'msj_tipo':msj_tipo,'msj_info':msj_info,'form':form}
		return render_to_response('form_usuario.html',info,context_instance=RequestContext(request))

	form = SolicitarCuenta()
	info = {'form':form}
	return render_to_response('form_usuario.html',info,context_instance=RequestContext(request))


@login_required(login_url='/')
def usuario_listar(request):
	listaU = Usuario.objects.order_by('-username')
	form = buscarUsuarioForm( initial={
		'habilitado': True
	})
	info = { 'listaU':listaU, 'form':form }
	return render_to_response('lista_usuarios.html',info,context_instance=RequestContext(request))


@login_required(login_url='/')
def usuario_editar(request, username):
	usuario = Usuario.objects.get(username=username)

	if (usuario.tipo == 'M') :
		usuario = Medico.objects.get(username=username)

	if request.method == 'POST':
		form = EditarCuenta(request.POST)
		if form.is_valid():
			pcd = form.cleaned_data

			if username.strip() == str(pcd['cedula']).strip() :
				validacion = True	
			else :
				prueba = Usuario.objects.filter(username=pcd['cedula'])
				if not prueba:
					validacion = True
				else : 
					validacion = False

			if validacion:
				if pcd['email'] == pcd['email0']:
					u_cambiarClave		= pcd['cambiarClave']
					u_clave_actual		= pcd['clave']
					u_clave_nueva		= pcd['claveNueva']
					u_clave_nueva0		= pcd['claveNueva0']
					usuario.username	= pcd['cedula']
					usuario.first_name	= pcd['nombres']
					usuario.last_name	= pcd['apellidos']
					usuario.email		= pcd['email']
					usuario.is_staff	= pcd['administrador']
					usuario.tipo		= pcd['tipo']

					if usuario.tipo == 'M' and pcd['codigoMedico'] == '' :
						msj_info = "Para el tipo de usuario 'Medico' el campo 'Codigo del medico' es requerido."

					else :
						if usuario.tipo == 'M' :
							usuario.codigo = pcd['codigoMedico']

						if u_cambiarClave:
							if usuario.check_password(u_clave_actual):
								if (u_clave_nueva == u_clave_nueva0):
									usuario.set_password(u_clave_nueva)
									usuario.save()
									return redirect("/usuario/listar")
								else:
									msj_info = "No hubo coincidencia con las claves nuevas ingresadas."
							else:
								msj_info = "La clave actual no es la correcta."  
						else:
							usuario.save()
							return redirect("/usuario/listar")
				else:
					msj_info = "No hubo coincidencia con los emails ingresados."  
			else :
				msj_info = "Ya hay un usuario registrado con esa cedula."
		else:
			msj_info = "Error con el formulario."
		
		msj_tipo = "danger"
		info = {'usuario':usuario, 'msj_tipo':msj_tipo, 'msj_info':msj_info, 'form':form}
		return render_to_response('form_usuario.html',info,context_instance=RequestContext(request))

	if (usuario.tipo == 'M') :
		form = EditarCuenta( initial={
			'cedula': usuario.username,
			'nombres': usuario.first_name,
			'apellidos': usuario.last_name,
			'email': usuario.email,
			'email0': usuario.email,
			'tipo': usuario.tipo,
			'administrador': usuario.is_staff,
			'codigoMedico' : usuario.codigo
		})
	else :
		form = EditarCuenta( initial={
			'cedula': usuario.username,
			'nombres': usuario.first_name,
			'apellidos': usuario.last_name,
			'email': usuario.email,
			'email0': usuario.email,
			'tipo': usuario.tipo,
			'administrador': usuario.is_staff
		})

	info = { 'usuario':usuario, 'form':form }
	return render_to_response('form_usuario.html',info,context_instance=RequestContext(request))


@login_required(login_url='/')
def usuario_buscar(request):
	if request.POST:
		form = buscarUsuarioForm(request.POST)
		if form.is_valid():
			pcd = form.cleaned_data
			values = [pcd['nombres'], pcd['apellidos'], pcd['cedula'], pcd['tipo'], pcd['habilitado']]
			fields = ["first_name", "last_name", "username", "tipo", "is_active"]
			Qr = None

			for v,f in itertools.izip(values, fields):
				if (v != "" and v!= None):

					if (f == "username"):
						q = Q(**{"%s__exact" % f : v })
					elif (f == "tipo" or f == "habilitado"):
						q = Q(**{"%s" % f : v })
					else:
						q = Q(**{"%s__icontains" % f : v })
					
					if Qr:
						Qr = Qr & q
					else:
						Qr = q 
			if Qr:
				users = Usuario.objects.filter(Qr)
			else:
				users = Usuario.objects.order_by('-username')
				
			formSearch = buscarUsuarioForm( initial={
				'habilitado': True
			})

			if len(users) > 0:
				info = { 'listaU':users, 'form':formSearch }

			else:
				msj_info = "Ningun usuario conincide con los criterios de busqueda."
				msj_tipo = "info"
				info = { 'listaU':users, 'form':formSearch, 'msj_tipo':msj_tipo, 'msj_info':msj_info}

			return render_to_response('lista_usuarios.html',info,context_instance=RequestContext(request))


@login_required(login_url='/')
def usuario_eliminar(request, cedulaU):
	element = Usuario.objects.get(username=cedulaU)
	element.delete()
	return redirect('/usuario/listar')


@login_required(login_url='/')
def usuario_habilitar(request,cedulaU):
	usuario = Usuario.objects.get(username=cedulaU)
	usuario.is_active = True
	usuario.save()
	return redirect("/usuario/listar")


@login_required(login_url='/')
def usuario_deshabilitar(request,cedulaU):
	usuario = Usuario.objects.get(username=cedulaU)
	usuario.is_active = False
	usuario.save()
	return redirect("/usuario/listar")


def usuario_solicitar(request):
	mensaje = ""
	form = IniciarSesionForm()
	if request.method == 'POST':
		formSolicitar = SolicitarCuenta(request.POST)
		if formSolicitar.is_valid():
			pcd = formSolicitar.cleaned_data
			u_tipo		       = pcd['tipo']
			u_codigoMedico	   = pcd['codigoMedico']
			u_cedula           = pcd['cedula']
			u_nombres          = pcd['nombres']
			u_apellidos        = pcd['apellidos']
			u_email            = pcd['email']
			u_email0           = pcd['email0']
			u_clave            = pcd['clave']
			u_clave0           = pcd['clave0']
			u_administrador    = pcd['administrador']

			prueba = Usuario.objects.filter(username=u_cedula)
			prueba2 = (u_clave==u_clave0)

			if not prueba:
				if prueba2:
					prueba2 = (u_email==u_email0)
					if prueba2:

						if u_tipo == 'M' and u_codigoMedico == '':
							msj_info = "Para el tipo de usuario 'Medico' el campo 'Codigo del medico' es requerido."
						
						else :
							u = None
							if u_tipo != 'M' : 
								u = Usuario(
									username=u_cedula,
									first_name=u_nombres,
									last_name=u_apellidos,
									tipo=u_tipo,
									email=u_email,
									password=u_clave
								)
							elif u_tipo == 'M' and u_codigoMedico:
								u = Medico(
									username=u_cedula,
									first_name=u_nombres,
									last_name=u_apellidos,
									tipo=u_tipo,
									codigo=u_codigoMedico,
									email=u_email,
									password=u_clave
								)
							u.is_active = False
							u.set_password(u_clave)
							if u_administrador == True:
								u.is_staff = True
							u.save()
							return redirect('/')

					else:
						msj_info = "No hubo coincidencia con los emails ingresados."     
				else:
					msj_info = "No hubo coincidencia con las claves ingresadas."     
			else:
				msj_info = "Ya hay un usuario registrado con esa cedula." 
		else:
			msj_info = "Error con el formulario."

		msj_tipo = "danger"
		info = {'msj_tipo':msj_tipo,'msj_info':msj_info,'form':form, 'formSolicitar':formSolicitar}
		return render_to_response('solicitar_cuenta.html',info,context_instance=RequestContext(request))

	formSolicitar = SolicitarCuenta()
	info = {'form':form, 'formSolicitar':formSolicitar}
	return render_to_response('solicitar_cuenta.html',info,context_instance=RequestContext(request))

@login_required(login_url='/')
def usario_listarPendientes(request):    
	listaP = Usuario.objects.all()
	info = {
		'listaP':listaP
		} 
	return render_to_response('usuarios_pendientes.html',info,context_instance=RequestContext(request))

@login_required(login_url='/')
def usario_listarRechazados(request):    
	listaP = Usuario.objects.filter(habilitado=False)
	info = {'listaP':listaP}
	return render_to_response('usuariosPendientes.html',info,context_instance=RequestContext(request))



@login_required(login_url='/')
def usuario_rechazar(request,cedulaU):
	usuario = get_object_or_404(Usuario,cedula=cedulaU)
	usuario.delete()
	return redirect("/usuario/pendientes")

@login_required(login_url='/')
def usuario_aprobar(request,cedulaU):
	usuario = get_object_or_404(Usuario,cedula=cedulaU)
	usuario.habilitado = True
	usuario.is_active = True
	usuario.save()
	email = EmailMessage('[GenSE] Admin - Activacion de Cuenta','Estimado/a '+usuario.first_name+' '+usuario.last_name+'\n\nSe aprobo su solicitud de activacion de cuenta\n\nSaludos,\nAdministrador del Sistema', to=[usuario.email]) 
	email.send()
	return redirect("/usuario/pendientes")

@login_required(login_url='/')
def pendiente_examinar(request,cedulaU):
	usuario = get_object_or_404(Usuario,cedula=cedulaU)
	info = {'usuario':usuario}
	return render_to_response('pendienteExaminar.html',info,context_instance=RequestContext(request))

@login_required(login_url='/')
def clave_cambiar(request):
	mensaje = ""
	if request.method == 'POST':
		form = cambioClave(request.POST)
		if form.is_valid():
			pcd = form.cleaned_data
			f_claveV          = pcd['claveV']
			f_clave           = pcd['clave']
			f_claveO          = pcd['claveO']
			usuario           = Usuario.objects.get(username=request.user)
			if usuario.check_password(f_claveV):
				if (f_clave == f_claveO):
					usuario.set_password(f_clave)
					usuario.save()
					mensaje = "Clave cambiada"
					form = cambioClave()
					info = {'form':form,'mensaje':mensaje}
					return render_to_response('cambiarClave.html',info,context_instance=RequestContext(request))                    
				else:
					mensaje = "Las dos claves son distintas"
			else:
				mensaje = "La clave antigua no es correcta"
		else:
			mensaje = "Error con el formulario"
		info = {'form':form,'mensaje':mensaje}
		return render_to_response('cambiarClave.html',info,context_instance=RequestContext(request))
	form = cambioClave()
	info = {'form':form,'mensaje':mensaje}
	return render_to_response('cambiarClave.html',info,context_instance=RequestContext(request))








from django.conf.urls import patterns, url, include

from views import *

urlpatterns = patterns('app_solicitudes.views',
    
    url('^habitacion/solicitar$','solicitar_habitacion'),
    url('^habitacion/paciente_nuevo$','solicitar_paciente_nuevo'),
    url('^buscar/paciente$','buscar_paciente_cedula'),
    url('^habitacion/listar_solicitudes','lista_solicitudes'),
)

#url('^habitacion/cancelarSolicitud$','lista_solicitudes'),

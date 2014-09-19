from django.conf.urls import patterns, url, include

from views import *

urlpatterns = patterns('app_camas.views',

    url('^habitacion/asignar$','asignar_habitacion'),
    url('^censo$','censo'),
    url('^habitacion/eliminarSolicitud$','eliminar_solicitud'),
    url('^habitacion/prueba$','prueba'),
)
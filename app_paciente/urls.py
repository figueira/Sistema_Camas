from django.conf.urls import patterns, url, include

from views import *

urlpatterns = patterns('app_paciente.views',

	url('^paciente/agregar/$','agregar_paciente'),
)
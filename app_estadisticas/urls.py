from django.conf.urls import patterns, url, include

from views import *

urlpatterns = patterns('app_estadisticas.views',

	url('^estadisticas/termometro/?(?P<dia>[0-9]+)?/?(?P<mes>[0-9]+)?/?(?P<ano>[0-9]+)?$','termometro'),
	url('^estadisticas/matriz$','matriz'),
   
)
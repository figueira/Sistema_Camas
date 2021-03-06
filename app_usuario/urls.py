from django.conf.urls import patterns, url, include

from views import *

urlpatterns = patterns('app_usuario.views',

    url('^$','sesion_iniciar'),
    url('^sesion/iniciar/$','sesion_iniciar'),
    url('^sesion/cerrar$','sesion_cerrar'),

    url('^usuario/solicitar$','usuario_solicitar'),
    url('^usuario/pendientes$','usario_listarPendientes'),
    url('^usuario/pendientes/(?P<cedulaU>\d+)/aprobar$', 'usuario_aprobar'),
    url('^usuario/pendientes/(?P<cedulaU>\d+)/rechazar$', 'usuario_rechazar'),
    url('^usuario/pendientes/(?P<cedulaU>\d+)/examinar$', 'pendiente_examinar'),
    url('^usuario/clave$','clave_cambiar'),
    url('^usuario/restablecer$','clave_restablecer'),
    url('^usuario/crear$','usuario_crear'),

    url('^usuario/listar$','usuario_listar'),
    url('^usuario/listar/buscar$','usuario_buscar'),
    url('^usuario/listar/(?P<cedulaU>\d+)/habilitar$', 'usuario_habilitar'),
    url('^usuario/listar/(?P<cedulaU>\d+)/deshabilitar$', 'usuario_deshabilitar'),
    url('^usuario/listar/(?P<username>\d+)/editar$', 'usuario_editar'),
    url('^usuario/listar/(?P<cedulaU>\d+)/borrar$', 'usuario_eliminar'),
)
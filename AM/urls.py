from django.conf.urls import patterns, include, url
from AM import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^', include('app_camas.urls')),
    url(r'^', include('app_solicitudes.urls')),
    url(r'^', include('app_usuario.urls')),
    url(r'^', include('app_estadisticas.urls')),
	url(r'^', include('app_paciente.urls')),
	
	(r'^selectable/', include('selectable.urls')),


    ## COSAS DJANGISTICAS
    # Admin
    url(r'^admin/', include(admin.site.urls)),
    # Media
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    # Static
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),


    # Examples:
    # url(r'^$', 'AM.views.home', name='home'),
    # url(r'^AM/', include('AM.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'backend.views.home', name='home'),
    # url(r'^tuneandolaweb_streaming/', include('tuneandolaweb_streaming.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^registrarEstudiante', "backend.views.registrar_estudiante",name="registrar_estudiante"),
    url(r'^consultar_estudiantes', "backend.views.consultar_estudiantes",name="consultar_estudiantes"),
    
    # Uncomment the next line to enable the admin: 
    url(r'^admin/', include(admin.site.urls)),
)

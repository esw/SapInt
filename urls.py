from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib.auth.views import password_reset
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    #url(r'^notificaciones/', include('notification.urls')),
    #url(r'^login/$', 'django.contrib.auth.views.login',{'template_name':'login.html'}, name="login"),
    #url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name="logout"),
    #url(r'^comentarios/', include('threadedcomments.urls')),
    #url(r'^users/',include('usuarios.urls')),
    #url(r'^importacion/',include('importacion.urls')),
    #url(r'^notifications/',include('notification.urls')),
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/chronograph/job/(?P<pk>\d+)/run/$','chronograph.views.job_run',name='admin_chronograph_job_run'),
    #url(r'^admin/obj_lookup/$','genericadmin.views.generic_lookup'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/', include('django.contrib.admin.urls')),
    url(r'^jsi18n/$', 'django.views.i18n.javascript_catalog'),
    #url(r'^index$', 'views.dashboard', name="index"),
    #url(r'^$', 'django.views.generic.simple.redirect_to',{'url':'index'}),
)

if settings.DEBUG:
    urlpatterns += patterns ('',
        url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^admin_media/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.ADMIN_MEDIA_ROOT, 'show_indexes': True}),
    )

if settings.DEBUG and ('test' in settings.INSTALLED_APPS):
    urlpatterns += patterns ('',
        url(r'^test/',include('test.urls')),
    )

#urlpatterns += patterns(
#(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', 
#{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#)

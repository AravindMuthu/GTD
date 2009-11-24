from django.conf.urls.defaults import *
from Todo.views import entry_todo,show_todo,todoform,entry_delete
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       ('^todo/$',todoform),
                       ('^entrytodb/$',entry_todo),
                       ('^getfromdb/$',show_todo),
                       ('^delete/$',entry_delete),
    # Example:
    # (r'^DjangoTodo/', include('DjangoTodo.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns +=patterns('',
                           ('^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)

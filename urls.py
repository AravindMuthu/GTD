from django.conf.urls.defaults import *
from Todo.views import entry_todo,show_todo,todoform,entry_delete,login,create_user,signup,logout,show,update,delete_item,debuginfo

from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       ('^$',login),
                       ('^GTD/$',login),
                       ('^login/$',login),
                       ('^signup/$',signup),
                       ('^create_user/$',create_user),
                       ('^todo/$',todoform),
                       ('^entrytodb/$',entry_todo),
                       ('^getfromdb/$',show_todo),
                       ('^delete/$',entry_delete),
                       ('^logout/$',logout),
                       ('^show/(?P<id>\d+)/$',show),
                       ('^update/(?P<id>\d+)/$',update),
                       ('^delete_item/(?P<id>\d+)/$',delete_item),
    # Example:
    # (r'^DjangoTodo/', include('DjangoTodo.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
                       (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns +=patterns('',
                           ('^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
                         
)




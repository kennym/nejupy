from django.conf.urls.static import static
from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'', include('competition.urls')),
    (r'', include('problem.urls')),
    (r'', include('submission.urls')),
    (r'', include('judge.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}, name='logout'),
) + static("media/", document_root=settings.MEDIA_ROOT)

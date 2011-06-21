from django.conf.urls.defaults import patterns, include, url
from manager import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'^problem/(\d+)$', views.problem_detail, name='problem_detail'),
    url(r'^problem/(\d+)/submit$', views.submit_to_problem, name='submit_to_problem'),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    #url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'competition/index.html'}, name='logout'),
)
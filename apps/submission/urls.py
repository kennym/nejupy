from django.conf.urls.defaults import patterns, include, url
from submission import views

urlpatterns = patterns('',
    url(r'^submission/(\d+)$', views.submission_detail, name='submission_detail'),
    url(r'^problem/(\d+)/submit$', views.submit_for_problem, name='submit_for_problem'),
)

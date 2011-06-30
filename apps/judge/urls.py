from django.conf.urls.defaults import patterns, include, url
from judge import views

urlpatterns = patterns('',
    url(r'^judge/dashboard$', views.judge_dashboard, name='judge_dashboard'),
)

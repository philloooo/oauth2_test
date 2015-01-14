from django.conf.urls import patterns, url

from auth import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'oauth2callback$',views.oauth2callback,name='oauth2callback'),
)

__author__ = 'wangweilong'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'blogapp.views.first_page'),
    url(r'^staff/', 'blogapp.views.staff'),
)

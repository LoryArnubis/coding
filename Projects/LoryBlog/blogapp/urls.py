__author__ = 'wangweilong'
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blogapp.views.first_page'),
    url(r'^staff/', 'blogapp.views.staff'),
    url(r'^templay', 'blogapp.views.templay'),
    url(r'^blogin/', 'blogapp.views.blogin'),
)

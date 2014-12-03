from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LoryBlog.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'LoryBlog.views.first_page'),
    url(r'^$', include('blogapp.urls')),
    #url(r'^blogapp/', include('blogapp.urls')),
    url(r'^templay/', include('blogapp.urls')),
    url(r'^blogin', include('blogapp.urls')),
    #url(r'^blog/', include('blog.urls')),
	(r'^site_media/(?P<path>.*)','django.views.static.serve',{'document_root':'/home/lory/Projects/coding/Projects/LoryBlog/templates/views'}),
)

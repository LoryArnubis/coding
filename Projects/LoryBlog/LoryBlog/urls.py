from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LoryBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'LoryBlog.views.first_page'),
    url(r'^blogapp/', include('blogapp.urls')),
    url(r'^templay/', include('blogapp.urls')),
)

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'hello.views.home'),
    url(r'^create$', 'hello.views.create_super_user'),
    url(r'^admin/', include(admin.site.urls)),
)

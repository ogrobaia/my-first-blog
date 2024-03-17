from django.conf.urls import patterns,include, url
from django.contrib import admin

urlpatterns = [

    url(r'^admin/',include(admin.site.urls)),
    url(r'^$', 'web.views.homepage', name="index"),

]

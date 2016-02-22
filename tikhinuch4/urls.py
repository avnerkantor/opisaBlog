from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = [
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^blog/', include('blog.urls')),
    url(r'^about/', 'blog.views.about', name='about'),
    # url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^accounts/', include('allauth.urls')),
    #url(r'^recent/$', views.recent, name='recent'),
]

from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import view_about, view_home, view_home_en, view_grunts, view_about_en, view_pisa

urlpatterns = [
    url(r'^$', view_home, name='home'),
    url(r'^en/', view_home_en),
    url(r'^blog/', include('blog.urls')),
    url(r'^en/blog/', include('blog.urls')),
    url(r'^about/', view_about, name='about'),
    url(r'^en/about/', view_about_en, name='about_en'),
    url(r'^grunts', view_grunts, name='grunts'),
    url(r'^pisa', view_pisa, name='pisa'),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

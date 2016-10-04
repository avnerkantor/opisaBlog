from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import post_list
from django.conf import settings
from django.conf.urls.static import static
from django.core.urlresolvers import reverse

urlpatterns = [
                  url(r'', include('blog.urls')),
                    # url(r'^$', view_home, name='home'),
                  # url(r'^en/', view_home_en),
                  # url(r'^new/', view_home_new),
                  # url(r'^blog/', include('blog.urls')),
                  # url(r'^en/blog/', include('blog.urls')),
                  # url(r'^about/', view_about, name='about'),
                  # url(r'^en/about/', view_about_en, name='about_en'),
                  # url(r'^grunts', view_grunts, name='grunts'),
                  # url(r'^pisa', view_pisa, name='pisa'),
                  # url(r'^polls/', include('polls.urls')),
                  url(r'^admin/', admin.site.urls),
                  url(r'^ckeditor/', include('ckeditor_uploader.urls')),
              ]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
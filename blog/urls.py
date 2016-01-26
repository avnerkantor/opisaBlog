from django.conf.urls import patterns, include, url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),
    # url(r'^recent/$', views.recent, name='recent'),
    # url(r'^category/(?P<slug>[\w-]+)/$', views.view_category, name='view_post_category'),
]

from django.conf.urls import patterns, include, url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.view_post_list, name='post_list'),
    url(r'^post/(?P<slug>[\w-]+)/$', views.view_post_detail, name='post_detail'),
]

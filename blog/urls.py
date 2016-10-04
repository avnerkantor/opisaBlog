from django.conf.urls import patterns, include, url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),
]

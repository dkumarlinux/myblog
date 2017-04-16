from django.conf.urls import url, include
from . import views
from .feeds import ArchiveFeed

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^(?P<id>\d+)/$', views.post_details, name='details'),
    url(r'^posts/$', views.posts, name='posts'),
    url(r'^feed/archive$', ArchiveFeed(), name='feed'),

]


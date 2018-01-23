from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.part_list),
        url(r'^part/(?P<pk>[0-9]+)/$', views.part_detail, name='part_detail'),
    ]

__author__ = 'zhangb3'

from django.conf.urls import url
from fibonacci import views

urlpatterns = [
    url(r'^fibonacci/$', views.fibonacci_show),
    url(r'^fibonacci/(.+)$', views.fibonacci_show),
]


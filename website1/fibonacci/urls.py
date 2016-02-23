__author__ = 'zhangb3'

from django.conf.urls import url
from fibonacci import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^fibonacci/$', views.fibonacci_show),
    url(r'^fibonacci/(.+)$', views.fibonacci_show),
]


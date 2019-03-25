from django.urls import path, re_path
from testurlapp import views

urlpatterns = [
    re_path(r'^users/(?P<month>[0-9]{2})/$', views.home_month),
    re_path(r'^users/(?P<month>[0-9]{2})/(?P<year>[0-9]{4})/$', views.home_year),
]
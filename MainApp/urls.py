from django.conf.urls import url
from MainApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Blog', views.blog, name='blog'),
    url(r'^Tips', views.tips, name='tips'),
    url(r'^SupportServices', views.supportservices, name='supportservices'),
    url(r'^Calendar', views.calendar, name='calendar'),
]

from django.conf.urls import url
from MainApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog', views.blog, name='blog'),
    url(r'^tips', views.tips, name='tips'),
    url(r'^support', views.support, name='support'),
    url(r'^calendar', views.calendar, name='calendar'),
    url(r'^login', views.login, name='login'),
    url(r'^submittip', views.submittip, name='submittip'),
]

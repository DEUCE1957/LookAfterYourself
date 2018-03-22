"""LookAfterYourself URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from MainApp import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^blog', views.blog, name='blog'),
    url(r'^tips', views.tips, name='tips'),
    url(r'^support', views.support, name='support'),
    url(r'^calendar', views.calendar, name='calendar'),
    url(r'^submittip', views.submittip, name='submittip'),
    url(r'^LookAfterYourself/', include('MainApp.urls')),
    url(r'^admin/',admin.site.urls),
    url(r'^event/(?P<eventID>[\w\-]+)/$', views.event, name='event'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$',views.register,name='register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^adhd', views.adhd, name='adhd'),
    url(r'^addiction', views.addiction, name='addiction'),
    url(r'^anxiety', views.anxiety, name='anxiety'),
    url(r'^bipolar', views.bipolar, name='bipolar'),
    url(r'^eatingdisorder', views.eatingdisorder, name='eatingdisorder'),
    url(r'^ocd', views.ocd, name='ocd'),
    url(r'^ptsd', views.ptsd, name='ptsd'),
    url(r'^general', views.general, name='general'),
    url(r'^depression', views.depression, name='depression'),
]
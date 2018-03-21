from django.conf.urls import url, include
from MainApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog', views.blog, name='blog'),
    url(r'^tips', views.tips, name='tips'),
    url(r'^support', views.support, name='support'),
    url(r'^calendar', views.calendar, name='calendar'),
    url(r'^submittip', views.submittip, name='submittip'),
    url(r'^event/(?P<eventID>[\w\-]+)/$', views.event, name='event'),
    url(r'^blog/', include('blog.urls')),
]

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
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^lazy_load_posts/$', views.lazy_load_posts, name='lazy_load_posts'),
]

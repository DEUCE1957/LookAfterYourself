from django.conf.urls import url, include
from MainApp.views import PostsListView, PostDetailView
from MainApp import views

urlpatterns = [
    url(r'^$', PostsListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
    url(r'^tips', views.tips, name='tips'),
    url(r'^support', views.support, name='support'),
    url(r'^calendar', views.calendar, name='calendar'),
    url(r'^submittip', views.submittip, name='submittip'),
    url(r'^suggestion', views.suggestion, name='suggestion'),
    url(r'^event/(?P<eventID>[\w\-]+)/$', views.event, name='event'),
    url(r'^search/', views.search, name='search'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^lazy_load_posts/$', views.lazy_load_posts, name='lazy_load_posts'),
    url(r'^depression', views.depression, name='depression'),
    url(r'^adhd', views.adhd, name='adhd'),
    url(r'^anxiety', views.anxiety, name='anxiety'),
    url(r'^bipolar', views.bipolar, name='bipolar'),
    url(r'^eatingdisorder', views.eatingdisorder, name='eatingdisorder'),
    url(r'^ocd', views.ocd, name='ocd'),
    url(r'^ptsd', views.ptsd, name='ptsd'),
    url(r'^general', views.general, name='general'),
    url(r'^addiction', views.addiction, name='addiction'),
]

# coding: utf-8
from django.conf.urls import url

from blog.views import PostsListView, PostDetailView

urlpatterns = [
    url(r'^$', PostsListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
]

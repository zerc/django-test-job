# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

from blog.views import PostsView, PostDetailView, TagsView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^posts/$', PostsView.as_view(), name="posts"),

    url(r'^posts/(?P<post_id>\d+)/$', PostDetailView.as_view(),
        name="post_detail"),

    url(r'posts/tag/(?P<slug>[\w\-_\d]+)/$',  TagsView.as_view(),
        name="posts_by_tag"),

    (r'^comments/', include('django.contrib.comments.urls'))
)

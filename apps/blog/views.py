# coding: utf-8
from django.views.generic import ListView, DetailView

from .models import Post, Tag


class PostsView(ListView):
    queryset = Post.objects.prefetch_related('tags')\
        .order_by('-created_datetime')
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_context_data(self, *args, **kwargs):
        context = super(ListView, self).get_context_data(*args, **kwargs)
        context['tags'] = Tag.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'
    template_name = 'post_detail.html'


class TagsView(PostsView):
    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

# coding: utf-8
from django.views.generic import ListView, DetailView, CreateView
from django.http import Http404
from django.db.models import Count

from .models import Post, Tag, Comment
from .forms import CommentForm


class PostsView(ListView):
    queryset = Post.objects.prefetch_related('tags')\
        .annotate(comments_count=Count('comment'))
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_context_data(self, *args, **kwargs):
        context = super(ListView, self).get_context_data(*args, **kwargs)
        context['tags'] = Tag.objects.all()
        return context


class PostDetailView(CreateView):
    form_class = CommentForm
    template_name = 'post_detail.html'

    @property
    def post_object(self):
        if self._post is False:
            try:
                self._post = Post.objects.filter(pk=self.kwargs['post_id'])\
                    .annotate(comments_count=Count('comment'))[0]
            except IndexError:
                raise Http404
        return self._post
    _post = False

    def get_context_data(self, *args, **kwargs):
        context = super(CreateView, self).get_context_data(*args, **kwargs)
        context['post'] = self.post_object
        context['comments'] = self.post_object.comment_set.all()
        return context

    def get_initial(self, *args, **kwargs):
        initial = super(CreateView, self).get_initial(*args, **kwargs)
        initial['post'] = self.post_object
        return initial

    def get_success_url(self):
        return self.post_object.get_absolute_url()


class TagsView(PostsView):
    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])\
                           .annotate(comments_count=Count('comment'))

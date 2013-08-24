# coding: utf-8
from django import test

from .models import Post, Tag


class PostsTest(test.TestCase):
    fixtures = ['initial.json']

    def test_post_list(self):
        response = self.client.get('/posts/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['posts']), 3)

    def test_post_detail(self):
        post = Post.objects.latest()
        response = self.client.get(post.get_absolute_url())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['post'].pk, post.pk)

    def test_tags(self):
        response = self.client.get('/posts/')
        self.assertEqual(len(response.context['tags']), 3)

    def test_posts_by_tag(self):
        tag = Tag.objects.get(pk=1)
        response = self.client.get(tag.get_absolute_url())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['posts']), tag.post_set.count())
        self.assertItemsEqual(
            sorted(response.context['posts'].values_list('pk', flat=True)),
            sorted(tag.post_set.values_list('pk', flat=True)))

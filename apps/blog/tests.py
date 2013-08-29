# coding: utf-8
from django import test

from .models import Post, Tag, Comment


class PostsTest(test.TestCase):
    fixtures = ['initial.json']

    def _get_post(self):
        return Post.objects.latest()

    def test_post_list(self):
        response = self.client.get('/posts/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['posts']), 3)

    def test_post_detail(self):
        post = self._get_post()
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

    def test_comments(self):
        post = self._get_post()
        response = self.client.get(post.get_absolute_url())

        self.assertEqual(response.context['post'].comment_set.count(), 0)

        response = self.client.post(post.get_absolute_url(), {'name': 'asdad'})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())

        response = self.client.post(post.get_absolute_url(), {
            'post': post.pk,
            'name': 'zero13cool',
            'text': 'Test comment'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.redirect_chain), 1)
        self.assertEqual(len(response.context['comments']), 1)

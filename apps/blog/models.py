# coding: utf-8
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length='225')
    text = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True)

    class Meta:
        get_latest_by = 'created_datetime'

    @models.permalink
    def get_absolute_url(self):
        return ('post_detail', (), {'post_id': self.pk})


class Tag(models.Model):
    title = models.CharField(max_length='225')
    slug = models.SlugField(max_length='255')
    descr = models.TextField()

    @models.permalink
    def get_absolute_url(self):
        return ('posts_by_tag', (), {'slug': self.slug})

    def __unicode__(self):
        return self.slug

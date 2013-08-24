# coding: utf-8
from django.contrib import admin

from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_datetime')
    list_per_page = 10
    filter_horizontal = ('tags',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)

# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'blog_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length='225')),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length='255')),
            ('descr', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'blog', ['Tag'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'blog_tag')


    models = {
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            'created_datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'225'"})
        },
        u'blog.tag': {
            'Meta': {'object_name': 'Tag'},
            'descr': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': "'255'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'225'"})
        }
    }

    complete_apps = ['blog']
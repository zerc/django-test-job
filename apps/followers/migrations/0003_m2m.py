# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

def get_users(model, string_ids):
    return model.objects.filter(pk__in=filter(None, string_ids.split(' ')))

class Migration(DataMigration):

    def forwards(self, orm):
        """
        Just fill through table
        """
        for man in orm.Man.objects.all():
            for _man in get_users(orm.Man, man.follow_ids):
                man.follow.add(_man)

    def backwards(self, orm):
        """
        Drop all created through table rows
        """
        for man in orm.Man.objects.all():
            man.follow.clear()

    models = {
        u'followers.man': {
            'Meta': {'object_name': 'Man', 'db_table': "'man_man'"},
            'follow': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'followers'", 'symmetrical': 'False', 'db_table': "'man_link'", 'to': u"orm['followers.Man']"}),
            'follow_ids': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'225'"})
        }
    }

    complete_apps = ['followers']
    symmetrical = True

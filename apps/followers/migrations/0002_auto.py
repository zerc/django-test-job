# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field follow on 'Man'
        m2m_table_name = 'man_link'
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_man', models.ForeignKey(orm[u'followers.man'], null=False)),
            ('to_man', models.ForeignKey(orm[u'followers.man'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_man_id', 'to_man_id'])


    def backwards(self, orm):
        # Removing M2M table for field follow on 'Man'
        db.delete_table('man_link')


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
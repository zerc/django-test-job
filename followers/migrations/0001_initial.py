# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Man'
        db.create_table('man_man', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='225')),
            ('follow_ids', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'followers', ['Man'])


    def backwards(self, orm):
        # Deleting model 'Man'
        db.delete_table('man_man')


    models = {
        u'followers.man': {
            'Meta': {'object_name': 'Man', 'db_table': "'man_man'"},
            'follow_ids': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'225'"})
        }
    }

    complete_apps = ['followers']
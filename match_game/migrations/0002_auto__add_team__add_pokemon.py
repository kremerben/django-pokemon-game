# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Team'
        db.create_table(u'match_game_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal(u'match_game', ['Team'])

        # Adding model 'Pokemon'
        db.create_table(u'match_game_pokemon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('pokedex_id', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['match_game.Team'])),
        ))
        db.send_create_signal(u'match_game', ['Pokemon'])


    def backwards(self, orm):
        # Deleting model 'Team'
        db.delete_table(u'match_game_team')

        # Deleting model 'Pokemon'
        db.delete_table(u'match_game_pokemon')


    models = {
        u'match_game.pokemon': {
            'Meta': {'object_name': 'Pokemon'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'pokedex_id': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['match_game.Team']"})
        },
        u'match_game.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['match_game']
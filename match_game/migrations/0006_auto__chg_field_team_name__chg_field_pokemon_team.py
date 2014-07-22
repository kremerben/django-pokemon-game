# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Team.name'
        db.alter_column(u'match_game_team', 'name', self.gf('django.db.models.fields.CharField')(default=1, max_length=120))

        # Changing field 'Pokemon.team'
        db.alter_column(u'match_game_pokemon', 'team_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['match_game.Team'], null=True))

    def backwards(self, orm):

        # Changing field 'Team.name'
        db.alter_column(u'match_game_team', 'name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))

        # Changing field 'Pokemon.team'
        db.alter_column(u'match_game_pokemon', 'team_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['match_game.Team']))

    models = {
        u'match_game.pokemon': {
            'Meta': {'object_name': 'Pokemon'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'pokedex_id': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['match_game.Team']", 'null': 'True', 'blank': 'True'})
        },
        u'match_game.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['match_game']
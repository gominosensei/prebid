# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Bid.bidderEmail'
        db.delete_column('prebid_bid', 'bidderEmail')

        # Deleting field 'Bid.bidderName'
        db.delete_column('prebid_bid', 'bidderName')

        # Adding field 'Bid.name'
        db.add_column('prebid_bid', 'name',
                      self.gf('django.db.models.fields.CharField')(default='foo', max_length=255),
                      keep_default=False)

        # Adding field 'Bid.email'
        db.add_column('prebid_bid', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Bid.bidderEmail'
        db.add_column('prebid_bid', 'bidderEmail',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True),
                      keep_default=False)

        # Adding field 'Bid.bidderName'
        db.add_column('prebid_bid', 'bidderName',
                      self.gf('django.db.models.fields.CharField')(default='foo', max_length=255),
                      keep_default=False)

        # Deleting field 'Bid.name'
        db.delete_column('prebid_bid', 'name')

        # Deleting field 'Bid.email'
        db.delete_column('prebid_bid', 'email')


    models = {
        'prebid.bid': {
            'Meta': {'object_name': 'Bid'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['prebid.Item']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('prebid.models.PhoneNumberField', [], {'default': "''", 'max_length': '20', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'prebid.item': {
            'Meta': {'object_name': 'Item'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minimumBid': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['prebid']
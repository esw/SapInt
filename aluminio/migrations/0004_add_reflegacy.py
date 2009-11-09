
from south.db import db
from django.db import models
from aluminio.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'RefLegacy'
        db.create_table('aluminio_reflegacy', (
            ('ref_legacy', orm['aluminio.reflegacy:ref_legacy']),
            ('referencia', orm['aluminio.reflegacy:referencia']),
            ('id', orm['aluminio.reflegacy:id']),
            ('sistema', orm['aluminio.reflegacy:sistema']),
        ))
        db.send_create_signal('aluminio', ['RefLegacy'])
        
        # Creating unique_together for [sistema, ref_legacy] on RefLegacy.
        db.create_unique('aluminio_reflegacy', ['sistema', 'ref_legacy'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'RefLegacy'
        db.delete_table('aluminio_reflegacy')
        
        # Deleting unique_together for [sistema, ref_legacy] on RefLegacy.
        db.delete_unique('aluminio_reflegacy', ['sistema', 'ref_legacy'])
        
    
    
    models = {
        'aluminio.referencia': {
            'aleacion_std': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Aleacion']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'perim_exp': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'perim_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'peso_lineal': ('django.db.models.fields.FloatField', [], {}),
            'temple_std': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Temple']", 'null': 'True', 'blank': 'True'})
        },
        'aluminio.temple': {
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'aluminio.aleacion': {
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'aluminio.sapaluminio': {
            'Meta': {'unique_together': "(('referencia', 'aleacion', 'temple', 'acabado', 'largo_mm'),)"},
            'acabado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Acabado']"}),
            'aleacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Aleacion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo_mm': ('django.db.models.fields.IntegerField', [], {}),
            'referencia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Referencia']"}),
            'temple': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Temple']"})
        },
        'aluminio.reflegacy': {
            'Meta': {'unique_together': "(('sistema', 'ref_legacy'),)"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ref_legacy': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'referencia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Referencia']"}),
            'sistema': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'aluminio.acabado': {
            'abreviacion': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['aluminio']

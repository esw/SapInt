
from south.db import db
from django.db import models
from aluminio.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'SapAluminio.tipo_mat'
        db.add_column('aluminio_sapaluminio', 'tipo_mat', orm['aluminio.sapaluminio:tipo_mat'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'SapAluminio.tipo_mat'
        db.delete_column('aluminio_sapaluminio', 'tipo_mat')
        
    
    
    models = {
        'aluminio.referencia': {
            'Meta': {'unique_together': "(('nombre',),)"},
            'aleacion_std': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Aleacion']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'perim_exp': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'perim_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'peso_lineal': ('django.db.models.fields.FloatField', [], {}),
            'temple_std': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Temple']", 'null': 'True', 'blank': 'True'})
        },
        'aluminio.reflegacy': {
            'Meta': {'unique_together': "(('sistema', 'ref_legacy'),)"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ref_legacy': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'referencia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Referencia']"}),
            'sistema': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'aluminio.aleacion': {
            'Meta': {'unique_together': "(('codigo',),)"},
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
            'temple': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Temple']"}),
            'tipo_mat': ('django.db.models.fields.CharField', [], {'default': "'FERT'", 'max_length': '6'})
        },
        'aluminio.temple': {
            'Meta': {'unique_together': "(('codigo',),)"},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'aluminio.acabado': {
            'Meta': {'unique_together': "(('nombre',),)"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['aluminio']

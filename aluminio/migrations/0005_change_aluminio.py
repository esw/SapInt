
from south.db import db
from django.db import models
from aluminio.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Deleting field 'Acabado.abreviacion'
        db.delete_column('aluminio_acabado', 'abreviacion')
        
        # Creating unique_together for [codigo] on Temple.
        db.create_unique('aluminio_temple', ['codigo'])
        
        # Creating unique_together for [codigo] on Aleacion.
        db.create_unique('aluminio_aleacion', ['codigo'])
        
        # Creating unique_together for [nombre] on Referencia.
        db.create_unique('aluminio_referencia', ['nombre'])
        
        # Creating unique_together for [nombre] on Acabado.
        db.create_unique('aluminio_acabado', ['nombre'])
        
    
    
    def backwards(self, orm):
        
        # Adding field 'Acabado.abreviacion'
        db.add_column('aluminio_acabado', 'abreviacion', orm['aluminio.acabado:abreviacion'])
        
        # Deleting unique_together for [codigo] on Temple.
        db.delete_unique('aluminio_temple', ['codigo'])
        
        # Deleting unique_together for [codigo] on Aleacion.
        db.delete_unique('aluminio_aleacion', ['codigo'])
        
        # Deleting unique_together for [nombre] on Referencia.
        db.delete_unique('aluminio_referencia', ['nombre'])
        
        # Deleting unique_together for [nombre] on Acabado.
        db.delete_unique('aluminio_acabado', ['nombre'])
        
    
    
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
            'temple': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Temple']"})
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

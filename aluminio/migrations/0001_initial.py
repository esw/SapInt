
from south.db import db
from django.db import models
from aluminio.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Referencia'
        db.create_table('aluminio_referencia', (
            ('perim_exp', orm['aluminio.Referencia:perim_exp']),
            ('peso_lineal', orm['aluminio.Referencia:peso_lineal']),
            ('temple_std', orm['aluminio.Referencia:temple_std']),
            ('aleacion_std', orm['aluminio.Referencia:aleacion_std']),
            ('nombre', orm['aluminio.Referencia:nombre']),
            ('perim_total', orm['aluminio.Referencia:perim_total']),
            ('id', orm['aluminio.Referencia:id']),
        ))
        db.send_create_signal('aluminio', ['Referencia'])
        
        # Adding model 'SapAluminio'
        db.create_table('aluminio_sapaluminio', (
            ('referencia', orm['aluminio.SapAluminio:referencia']),
            ('largo_mm', orm['aluminio.SapAluminio:largo_mm']),
            ('acabado', orm['aluminio.SapAluminio:acabado']),
            ('temple', orm['aluminio.SapAluminio:temple']),
            ('aleacion', orm['aluminio.SapAluminio:aleacion']),
            ('id', orm['aluminio.SapAluminio:id']),
        ))
        db.send_create_signal('aluminio', ['SapAluminio'])
        
        # Adding model 'Aleacion'
        db.create_table('aluminio_aleacion', (
            ('codigo', orm['aluminio.Aleacion:codigo']),
            ('id', orm['aluminio.Aleacion:id']),
        ))
        db.send_create_signal('aluminio', ['Aleacion'])
        
        # Adding model 'Temple'
        db.create_table('aluminio_temple', (
            ('codigo', orm['aluminio.Temple:codigo']),
            ('id', orm['aluminio.Temple:id']),
        ))
        db.send_create_signal('aluminio', ['Temple'])
        
        # Adding model 'Acabado'
        db.create_table('aluminio_acabado', (
            ('nombre', orm['aluminio.Acabado:nombre']),
            ('id', orm['aluminio.Acabado:id']),
            ('abreviacion', orm['aluminio.Acabado:abreviacion']),
        ))
        db.send_create_signal('aluminio', ['Acabado'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Referencia'
        db.delete_table('aluminio_referencia')
        
        # Deleting model 'SapAluminio'
        db.delete_table('aluminio_sapaluminio')
        
        # Deleting model 'Aleacion'
        db.delete_table('aluminio_aleacion')
        
        # Deleting model 'Temple'
        db.delete_table('aluminio_temple')
        
        # Deleting model 'Acabado'
        db.delete_table('aluminio_acabado')
        
    
    
    models = {
        'aluminio.referencia': {
            'aleacion_std': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Aleacion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'perim_exp': ('django.db.models.fields.FloatField', [], {}),
            'perim_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'peso_lineal': ('django.db.models.fields.FloatField', [], {}),
            'temple_std': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Temple']"})
        },
        'aluminio.sapaluminio': {
            'acabado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Acabado']"}),
            'aleacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Aleacion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo_mm': ('django.db.models.fields.IntegerField', [], {}),
            'referencia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Referencia']"}),
            'temple': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Temple']"})
        },
        'aluminio.aleacion': {
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'aluminio.temple': {
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'aluminio.acabado': {
            'abreviacion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['aluminio']


from south.db import db
from django.db import models
from aluminio.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'Referencia.perim_exp'
        # (to signature: django.db.models.fields.FloatField(null=True, blank=True))
        db.alter_column('aluminio_referencia', 'perim_exp', orm['aluminio.referencia:perim_exp'])
        
        # Changing field 'Referencia.temple_std'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['aluminio.Temple'], null=True, blank=True))
        db.alter_column('aluminio_referencia', 'temple_std_id', orm['aluminio.referencia:temple_std'])
        
        # Changing field 'Referencia.aleacion_std'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['aluminio.Aleacion'], null=True, blank=True))
        db.alter_column('aluminio_referencia', 'aleacion_std_id', orm['aluminio.referencia:aleacion_std'])
        
        # Changing field 'Acabado.abreviacion'
        # (to signature: django.db.models.fields.CharField(max_length=20, null=True, blank=True))
        db.alter_column('aluminio_acabado', 'abreviacion', orm['aluminio.acabado:abreviacion'])
        
    
    
    def backwards(self, orm):
        
        # Changing field 'Referencia.perim_exp'
        # (to signature: django.db.models.fields.FloatField())
        db.alter_column('aluminio_referencia', 'perim_exp', orm['aluminio.referencia:perim_exp'])
        
        # Changing field 'Referencia.temple_std'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['aluminio.Temple']))
        db.alter_column('aluminio_referencia', 'temple_std_id', orm['aluminio.referencia:temple_std'])
        
        # Changing field 'Referencia.aleacion_std'
        # (to signature: django.db.models.fields.related.ForeignKey(to=orm['aluminio.Aleacion']))
        db.alter_column('aluminio_referencia', 'aleacion_std_id', orm['aluminio.referencia:aleacion_std'])
        
        # Changing field 'Acabado.abreviacion'
        # (to signature: django.db.models.fields.CharField(max_length=20))
        db.alter_column('aluminio_acabado', 'abreviacion', orm['aluminio.acabado:abreviacion'])
        
    
    
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
        'aluminio.sapaluminio': {
            'Meta': {'unique_together': "(('referencia', 'aleacion', 'temple', 'acabado', 'largo_mm'),)"},
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
            'abreviacion': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['aluminio']

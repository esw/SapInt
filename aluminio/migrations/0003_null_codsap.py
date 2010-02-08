
from south.db import db
from django.db import models
from aluminio.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'SapAluminio.cod_sap'
        # (to signature: django.db.models.fields.CharField(max_length=50, null=True, blank=True))
        db.alter_column('aluminio_sapaluminio', 'cod_sap', orm['aluminio.sapaluminio:cod_sap'])
        
        # Deleting unique_together for [cod_sap] on sapaluminio.
        db.delete_unique('aluminio_sapaluminio', ['cod_sap'])
        
    
    
    def backwards(self, orm):
        
        # Changing field 'SapAluminio.cod_sap'
        # (to signature: django.db.models.fields.CharField(max_length=50))
        db.alter_column('aluminio_sapaluminio', 'cod_sap', orm['aluminio.sapaluminio:cod_sap'])
        
        # Creating unique_together for [cod_sap] on sapaluminio.
        db.create_unique('aluminio_sapaluminio', ['cod_sap'])
        
    
    
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
        'aluminio.aleacion': {
            'Meta': {'unique_together': "(('codigo',),)"},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'aluminio.referenciasant': {
            'Meta': {'unique_together': "(('sistema', 'ref_ant'),)"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'peso_lineal': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'ref_ant': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'referencia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Referencia']"}),
            'sistema': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'aluminio.sapaluminio': {
            'Meta': {'unique_together': "(('referencia', 'aleacion', 'temple', 'acabado', 'largo_mm', 'tipo_mat'),)"},
            'acabado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Acabado']"}),
            'aleacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Aleacion']"}),
            'cargado': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'cod_sap': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
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
        'aluminio.tipoacabado': {
            'Meta': {'unique_together': "(('nombre',),)"},
            'cons_calc': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'primer': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
        },
        'aluminio.acabadosant': {
            'Meta': {'unique_together': "(('sistema', 'acab_ant'),)"},
            'acab_ant': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'acabado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Acabado']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sistema': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'aluminio.sistemaant': {
            'Meta': {'unique_together': "(('nombre',),)"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'aluminio.acabado': {
            'Meta': {'unique_together': "(('nombre',),)"},
            'cod_epics': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'cod_sap_mat': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.TipoAcabado']", 'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['aluminio']


from south.db import db
from django.db import models
from aluminio.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'GrupoValoracion'
        db.create_table('aluminio_grupovaloracion', (
            ('valor_total', orm['aluminio.grupovaloracion:valor_total']),
            ('codigo', orm['aluminio.grupovaloracion:codigo']),
            ('peso_total_kg', orm['aluminio.grupovaloracion:peso_total_kg']),
            ('id', orm['aluminio.grupovaloracion:id']),
        ))
        db.send_create_signal('aluminio', ['GrupoValoracion'])
        
        # Adding field 'Acabado.grupo_val'
        db.add_column('aluminio_acabado', 'grupo_val', orm['aluminio.acabado:grupo_val'])
        
        # Creating unique_together for [codigo] on GrupoValoracion.
        db.create_unique('aluminio_grupovaloracion', ['codigo'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'GrupoValoracion'
        db.delete_table('aluminio_grupovaloracion')
        
        # Deleting field 'Acabado.grupo_val'
        db.delete_column('aluminio_acabado', 'grupo_val_id')
        
        # Deleting unique_together for [codigo] on GrupoValoracion.
        db.delete_unique('aluminio_grupovaloracion', ['codigo'])
        
    
    
    models = {
        'aluminio.referencia': {
            'Meta': {'unique_together': "(('nombre',),)"},
            'aleacion_std': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Aleacion']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'perim_exp': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'perim_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'peso_lineal': ('django.db.models.fields.FloatField', [], {}),
            'temple_std': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.Temple']", 'null': 'True', 'blank': 'True'}),
            'unbw': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
        },
        'aluminio.grupovaloracion': {
            'Meta': {'unique_together': "(('codigo',),)"},
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'peso_total_kg': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'valor_total': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'aluminio.ubicacionsap': {
            'Meta': {'unique_together': "(('codigo',),)"},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
        'aluminio.ubicacionsant': {
            'Meta': {'unique_together': "(('sistema', 'ubicacion_ant'),)"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sistema': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ubicacion_ant': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ubicacion_sap': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.UbicacionSap']"})
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
        'aluminio.acabado': {
            'Meta': {'unique_together': "(('nombre',),)"},
            'cod_epics': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'cod_sap_mat': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'grupo_val': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.GrupoValoracion']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.TipoAcabado']", 'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['aluminio']

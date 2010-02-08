
from south.db import db
from django.db import models
from aluminio.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'UbicacionSap'
        db.create_table('aluminio_ubicacionsap', (
            ('codigo', orm['aluminio.ubicacionsap:codigo']),
            ('id', orm['aluminio.ubicacionsap:id']),
        ))
        db.send_create_signal('aluminio', ['UbicacionSap'])
        
        # Adding model 'UbicacionSAnt'
        db.create_table('aluminio_ubicacionsant', (
            ('ubicacion_sap', orm['aluminio.ubicacionsant:ubicacion_sap']),
            ('ubicacion_ant', orm['aluminio.ubicacionsant:ubicacion_ant']),
            ('id', orm['aluminio.ubicacionsant:id']),
            ('sistema', orm['aluminio.ubicacionsant:sistema']),
        ))
        db.send_create_signal('aluminio', ['UbicacionSAnt'])
        
        # Deleting model 'sistemaant'
        db.delete_table('aluminio_sistemaant')
        
        # Creating unique_together for [sistema, ubicacion_ant] on UbicacionSAnt.
        db.create_unique('aluminio_ubicacionsant', ['sistema', 'ubicacion_ant'])
        
        # Creating unique_together for [codigo] on UbicacionSap.
        db.create_unique('aluminio_ubicacionsap', ['codigo'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'UbicacionSap'
        db.delete_table('aluminio_ubicacionsap')
        
        # Deleting model 'UbicacionSAnt'
        db.delete_table('aluminio_ubicacionsant')
        
        # Adding model 'sistemaant'
        db.create_table('aluminio_sistemaant', (
            ('nombre', orm['aluminio.ubicacionsant:nombre']),
            ('id', orm['aluminio.ubicacionsant:id']),
        ))
        db.send_create_signal('aluminio', ['sistemaant'])
        
        # Deleting unique_together for [sistema, ubicacion_ant] on UbicacionSAnt.
        db.delete_unique('aluminio_ubicacionsant', ['sistema', 'ubicacion_ant'])
        
        # Deleting unique_together for [codigo] on UbicacionSap.
        db.delete_unique('aluminio_ubicacionsap', ['codigo'])
        
    
    
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
        'aluminio.ubicacionsap': {
            'Meta': {'unique_together': "(('codigo',),)"},
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aluminio.TipoAcabado']", 'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['aluminio']

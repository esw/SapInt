
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
        
        # Adding model 'Aleacion'
        db.create_table('aluminio_aleacion', (
            ('codigo', orm['aluminio.Aleacion:codigo']),
            ('id', orm['aluminio.Aleacion:id']),
        ))
        db.send_create_signal('aluminio', ['Aleacion'])
        
        # Adding model 'ReferenciaSAnt'
        db.create_table('aluminio_referenciasant', (
            ('ref_ant', orm['aluminio.ReferenciaSAnt:ref_ant']),
            ('referencia', orm['aluminio.ReferenciaSAnt:referencia']),
            ('peso_lineal', orm['aluminio.ReferenciaSAnt:peso_lineal']),
            ('id', orm['aluminio.ReferenciaSAnt:id']),
            ('sistema', orm['aluminio.ReferenciaSAnt:sistema']),
        ))
        db.send_create_signal('aluminio', ['ReferenciaSAnt'])
        
        # Adding model 'Temple'
        db.create_table('aluminio_temple', (
            ('codigo', orm['aluminio.Temple:codigo']),
            ('id', orm['aluminio.Temple:id']),
        ))
        db.send_create_signal('aluminio', ['Temple'])
        
        # Adding model 'TipoAcabado'
        db.create_table('aluminio_tipoacabado', (
            ('cons_calc', orm['aluminio.TipoAcabado:cons_calc']),
            ('nombre', orm['aluminio.TipoAcabado:nombre']),
            ('primer', orm['aluminio.TipoAcabado:primer']),
            ('id', orm['aluminio.TipoAcabado:id']),
        ))
        db.send_create_signal('aluminio', ['TipoAcabado'])
        
        # Adding model 'AcabadoSAnt'
        db.create_table('aluminio_acabadosant', (
            ('acab_ant', orm['aluminio.AcabadoSAnt:acab_ant']),
            ('id', orm['aluminio.AcabadoSAnt:id']),
            ('acabado', orm['aluminio.AcabadoSAnt:acabado']),
            ('sistema', orm['aluminio.AcabadoSAnt:sistema']),
        ))
        db.send_create_signal('aluminio', ['AcabadoSAnt'])
        
        # Adding model 'SistemaAnt'
        db.create_table('aluminio_sistemaant', (
            ('nombre', orm['aluminio.SistemaAnt:nombre']),
            ('id', orm['aluminio.SistemaAnt:id']),
        ))
        db.send_create_signal('aluminio', ['SistemaAnt'])
        
        # Adding model 'Acabado'
        db.create_table('aluminio_acabado', (
            ('nombre', orm['aluminio.Acabado:nombre']),
            ('cod_epics', orm['aluminio.Acabado:cod_epics']),
            ('id', orm['aluminio.Acabado:id']),
            ('tipo', orm['aluminio.Acabado:tipo']),
            ('cod_sap_mat', orm['aluminio.Acabado:cod_sap_mat']),
        ))
        db.send_create_signal('aluminio', ['Acabado'])
        
        # Creating unique_together for [nombre] on TipoAcabado.
        db.create_unique('aluminio_tipoacabado', ['nombre'])
        
        # Creating unique_together for [codigo] on Aleacion.
        db.create_unique('aluminio_aleacion', ['codigo'])
        
        # Creating unique_together for [sistema, acab_ant] on AcabadoSAnt.
        db.create_unique('aluminio_acabadosant', ['sistema', 'acab_ant'])
        
        # Creating unique_together for [codigo] on Temple.
        db.create_unique('aluminio_temple', ['codigo'])
        
        # Creating unique_together for [nombre] on SistemaAnt.
        db.create_unique('aluminio_sistemaant', ['nombre'])
        
        # Creating unique_together for [sistema, ref_ant] on ReferenciaSAnt.
        db.create_unique('aluminio_referenciasant', ['sistema', 'ref_ant'])
        
        # Creating unique_together for [nombre] on Referencia.
        db.create_unique('aluminio_referencia', ['nombre'])
        
        # Creating unique_together for [nombre] on Acabado.
        db.create_unique('aluminio_acabado', ['nombre'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Referencia'
        db.delete_table('aluminio_referencia')
        
        # Deleting model 'Aleacion'
        db.delete_table('aluminio_aleacion')
        
        # Deleting model 'ReferenciaSAnt'
        db.delete_table('aluminio_referenciasant')
        
        # Deleting model 'Temple'
        db.delete_table('aluminio_temple')
        
        # Deleting model 'TipoAcabado'
        db.delete_table('aluminio_tipoacabado')
        
        # Deleting model 'AcabadoSAnt'
        db.delete_table('aluminio_acabadosant')
        
        # Deleting model 'SistemaAnt'
        db.delete_table('aluminio_sistemaant')
        
        # Deleting model 'Acabado'
        db.delete_table('aluminio_acabado')
        
        # Deleting unique_together for [nombre] on TipoAcabado.
        db.delete_unique('aluminio_tipoacabado', ['nombre'])
        
        # Deleting unique_together for [codigo] on Aleacion.
        db.delete_unique('aluminio_aleacion', ['codigo'])
        
        # Deleting unique_together for [sistema, acab_ant] on AcabadoSAnt.
        db.delete_unique('aluminio_acabadosant', ['sistema', 'acab_ant'])
        
        # Deleting unique_together for [codigo] on Temple.
        db.delete_unique('aluminio_temple', ['codigo'])
        
        # Deleting unique_together for [nombre] on SistemaAnt.
        db.delete_unique('aluminio_sistemaant', ['nombre'])
        
        # Deleting unique_together for [sistema, ref_ant] on ReferenciaSAnt.
        db.delete_unique('aluminio_referenciasant', ['sistema', 'ref_ant'])
        
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

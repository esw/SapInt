
from south.db import db
from django.db import models
from sapcat.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Centro'
        db.create_table('sapcat_centro', (
            ('cod_sap', orm['sapcat.Centro:cod_sap']),
            ('nombre', orm['sapcat.Centro:nombre']),
            ('id', orm['sapcat.Centro:id']),
        ))
        db.send_create_signal('sapcat', ['Centro'])
        
        # Adding model 'TipoMaterial'
        db.create_table('sapcat_tipomaterial', (
            ('nombre', orm['sapcat.TipoMaterial:nombre']),
            ('id', orm['sapcat.TipoMaterial:id']),
        ))
        db.send_create_signal('sapcat', ['TipoMaterial'])
        
        # Adding model 'ParamsMaterial'
        db.create_table('sapcat_paramsmaterial', (
            ('division', orm['sapcat.ParamsMaterial:division']),
            ('tipo_mat', orm['sapcat.ParamsMaterial:tipo_mat']),
            ('matl_grp', orm['sapcat.ParamsMaterial:matl_grp']),
            ('indt_sect', orm['sapcat.ParamsMaterial:indt_sect']),
            ('gen_item_cat_grp', orm['sapcat.ParamsMaterial:gen_item_cat_grp']),
            ('id', orm['sapcat.ParamsMaterial:id']),
            ('base_uom', orm['sapcat.ParamsMaterial:base_uom']),
        ))
        db.send_create_signal('sapcat', ['ParamsMaterial'])
        
        # Creating unique_together for [nombre] on Centro.
        db.create_unique('sapcat_centro', ['nombre'])
        
        # Creating unique_together for [tipo_mat] on ParamsMaterial.
        db.create_unique('sapcat_paramsmaterial', ['tipo_mat_id'])
        
        # Creating unique_together for [nombre] on TipoMaterial.
        db.create_unique('sapcat_tipomaterial', ['nombre'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Centro'
        db.delete_table('sapcat_centro')
        
        # Deleting model 'TipoMaterial'
        db.delete_table('sapcat_tipomaterial')
        
        # Deleting model 'ParamsMaterial'
        db.delete_table('sapcat_paramsmaterial')
        
        # Deleting unique_together for [nombre] on Centro.
        db.delete_unique('sapcat_centro', ['nombre'])
        
        # Deleting unique_together for [tipo_mat] on ParamsMaterial.
        db.delete_unique('sapcat_paramsmaterial', ['tipo_mat_id'])
        
        # Deleting unique_together for [nombre] on TipoMaterial.
        db.delete_unique('sapcat_tipomaterial', ['nombre'])
        
    
    
    models = {
        'sapcat.centro': {
            'Meta': {'unique_together': "(('nombre',),)"},
            'cod_sap': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'sapcat.tipomaterial': {
            'Meta': {'unique_together': "(('nombre',),)"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'sapcat.paramsmaterial': {
            'Meta': {'unique_together': "(('tipo_mat',),)"},
            'base_uom': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'division': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'gen_item_cat_grp': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indt_sect': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'matl_grp': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'tipo_mat': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sapcat.TipoMaterial']"})
        }
    }
    
    complete_apps = ['sapcat']

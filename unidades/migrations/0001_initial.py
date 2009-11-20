
from south.db import db
from django.db import models
from unidades.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'SistemaMedida'
        db.create_table('unidades_sistemamedida', (
            ('id', models.AutoField(primary_key=True)),
            ('abrev_en', models.CharField(_('Abreviacion (Ing)'), max_length=5)),
            ('nombre_en', models.CharField(_('Nombre (Ing)'), max_length=150)),
            ('nombre_es', models.CharField(_('Nombre (Esp)'), max_length=150)),
            ('ref', models.CharField(_('Referencia'), max_length=5)),
            ('abrev_es', models.CharField(_('Abreviacion (Esp)'), max_length=5)),
        ))
        db.send_create_signal('unidades', ['SistemaMedida'])
        
        # Adding model 'UnidadTipoSistema'
        db.create_table('unidades_unidadtiposistema', (
            ('id', models.AutoField(primary_key=True)),
            ('unidad', models.ForeignKey(orm.UnidadMedida, verbose_name=_('Unidad'))),
            ('tipo', models.ForeignKey(orm.TipoUnidad, verbose_name=_('Tipo'))),
            ('sistema', models.ForeignKey(orm.SistemaMedida, verbose_name=_('Sistema'))),
        ))
        db.send_create_signal('unidades', ['UnidadTipoSistema'])
        
        # Adding model 'TipoUnidad'
        db.create_table('unidades_tipounidad', (
            ('id', models.AutoField(primary_key=True)),
            ('abrev_en', models.CharField(_('Abreviacion (Ing)'), max_length=5)),
            ('nombre_en', models.CharField(_('Nombre (Ing)'), max_length=150)),
            ('nombre_es', models.CharField(_('Nombre (Esp)'), max_length=150)),
            ('ref', models.CharField(_('Referencia'), max_length=5)),
            ('abrev_es', models.CharField(_('Abreviacion (Esp)'), max_length=5)),
        ))
        db.send_create_signal('unidades', ['TipoUnidad'])
        
        # Adding model 'Conversion'
        db.create_table('unidades_conversion', (
            ('id', models.AutoField(primary_key=True)),
            ('unidad_origen', models.ForeignKey(orm.UnidadMedida, related_name='u_origen', verbose_name=_('Unidad Origen'))),
            ('unidad_destino', models.ForeignKey(orm.UnidadMedida, related_name='u_destino', verbose_name=_('Unidad Destino'))),
            ('factor', models.DecimalField(default=0, max_digits=30, decimal_places=10)),
        ))
        db.send_create_signal('unidades', ['Conversion'])
        
        # Adding model 'UnidadMedida'
        db.create_table('unidades_unidadmedida', (
            ('id', models.AutoField(primary_key=True)),
            ('abrev_en', models.CharField(_('Abreviacion (Ing)'), max_length=5)),
            ('tipo', models.ForeignKey(orm.TipoUnidad, related_name='unidades', verbose_name=_('Tipo Unidad'))),
            ('nombre_en', models.CharField(_('Nombre (Ing)'), max_length=150)),
            ('nombre_es', models.CharField(_('Nombre (Esp)'), max_length=150)),
            ('sistema', models.ForeignKey(orm.SistemaMedida, related_name='unidades', verbose_name=_('Sistema'))),
            ('ref', models.CharField(_('Referencia'), max_length=5)),
            ('abrev_es', models.CharField(_('Abreviacion (Esp)'), max_length=5)),
        ))
        db.send_create_signal('unidades', ['UnidadMedida'])
        
        # Creating unique_together for [sistema, tipo] on UnidadTipoSistema.
        db.create_unique('unidades_unidadtiposistema', ['sistema_id', 'tipo_id'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'SistemaMedida'
        db.delete_table('unidades_sistemamedida')
        
        # Deleting model 'UnidadTipoSistema'
        db.delete_table('unidades_unidadtiposistema')
        
        # Deleting model 'TipoUnidad'
        db.delete_table('unidades_tipounidad')
        
        # Deleting model 'Conversion'
        db.delete_table('unidades_conversion')
        
        # Deleting model 'UnidadMedida'
        db.delete_table('unidades_unidadmedida')
        
        # Deleting unique_together for [sistema, tipo] on UnidadTipoSistema.
        db.delete_unique('unidades_unidadtiposistema', ['sistema_id', 'tipo_id'])
        
    
    
    models = {
        'unidades.sistemamedida': {
            'Meta': {'ordering': "['ref']"},
            'abrev_en': ('models.CharField', ["_('Abreviacion (Ing)')"], {'max_length': '5'}),
            'abrev_es': ('models.CharField', ["_('Abreviacion (Esp)')"], {'max_length': '5'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'nombre_en': ('models.CharField', ["_('Nombre (Ing)')"], {'max_length': '150'}),
            'nombre_es': ('models.CharField', ["_('Nombre (Esp)')"], {'max_length': '150'}),
            'ref': ('models.CharField', ["_('Referencia')"], {'max_length': '5'}),
            'unidades_tipo': ('models.ManyToManyField', ["'TipoUnidad'"], {'null': 'True', 'through': "'UnidadTipoSistema'", 'blank': 'True'})
        },
        'unidades.unidadtiposistema': {
            'Meta': {'ordering': "['sistema','tipo','unidad']", 'unique_together': "(('sistema','tipo'),)"},
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'sistema': ('models.ForeignKey', ['SistemaMedida'], {'verbose_name': "_('Sistema')"}),
            'tipo': ('models.ForeignKey', ['TipoUnidad'], {'verbose_name': "_('Tipo')"}),
            'unidad': ('models.ForeignKey', ['UnidadMedida'], {'verbose_name': "_('Unidad')"})
        },
        'unidades.tipounidad': {
            'Meta': {'ordering': "['ref']"},
            'abrev_en': ('models.CharField', ["_('Abreviacion (Ing)')"], {'max_length': '5'}),
            'abrev_es': ('models.CharField', ["_('Abreviacion (Esp)')"], {'max_length': '5'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'nombre_en': ('models.CharField', ["_('Nombre (Ing)')"], {'max_length': '150'}),
            'nombre_es': ('models.CharField', ["_('Nombre (Esp)')"], {'max_length': '150'}),
            'ref': ('models.CharField', ["_('Referencia')"], {'max_length': '5'})
        },
        'unidades.conversion': {
            'Meta': {'ordering': "['unidad_origen','unidad_destino']"},
            'factor': ('models.DecimalField', [], {'default': '0', 'max_digits': '30', 'decimal_places': '10'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'unidad_destino': ('models.ForeignKey', ['UnidadMedida'], {'related_name': "'u_destino'", 'verbose_name': "_('Unidad Destino')"}),
            'unidad_origen': ('models.ForeignKey', ['UnidadMedida'], {'related_name': "'u_origen'", 'verbose_name': "_('Unidad Origen')"})
        },
        'unidades.unidadmedida': {
            'Meta': {'ordering': "['sistema','tipo','ref']"},
            'abrev_en': ('models.CharField', ["_('Abreviacion (Ing)')"], {'max_length': '5'}),
            'abrev_es': ('models.CharField', ["_('Abreviacion (Esp)')"], {'max_length': '5'}),
            'conversiones': ('models.ManyToManyField', ["'self'"], {'through': "'Conversion'", 'verbose_name': "_('Conversiones')", 'symmetrical': 'False'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'nombre_en': ('models.CharField', ["_('Nombre (Ing)')"], {'max_length': '150'}),
            'nombre_es': ('models.CharField', ["_('Nombre (Esp)')"], {'max_length': '150'}),
            'ref': ('models.CharField', ["_('Referencia')"], {'max_length': '5'}),
            'sistema': ('models.ForeignKey', ['SistemaMedida'], {'related_name': "'unidades'", 'verbose_name': "_('Sistema')"}),
            'tipo': ('models.ForeignKey', ['TipoUnidad'], {'related_name': "'unidades'", 'verbose_name': "_('Tipo Unidad')"})
        }
    }
    
    complete_apps = ['unidades']

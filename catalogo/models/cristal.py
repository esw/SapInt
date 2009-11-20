
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from unidades.fields import MedidaModelField
from unidades.models import TipoUnidad, UnidadMedida
from base.helpers import getself_trans
from unidades.medida import *
 
__all__ = [
    'ComposicionCristal',
    'CristalTratamiento',
    'CristalColor',
    'CristalAcabado',
    'CristalEspesor',
    'CristalColorEspesor',
    'SeparadorTipo',
    'SeparadorMaterial',
    'SeparadorEspesor',
    'ItemComposicion',
    'Cristal',
    'Separador',
]
 
class ComposicionCristal(models.Model):
    desc_in_en = models.TextField(_('Descripcion in (Ing)'))
    desc_in_es = models.TextField(_('Descripcion in (Esp)'))
    desc_mm_en = models.TextField(_('Descripcion mm (Ing)'))
    desc_mm_es = models.TextField(_('Descripcion mm (Esp)'))
    composicion_hash = models.CharField(_('Composicion Hash'), max_length=200, editable=False)
 
    class Meta:
        app_label = 'catalogo'
        verbose_name = _('Composicion Cristal')
        verbose_name_plural = _('Composicion Cristal')
        unique_together = ('composicion_hash',)
    def __unicode__(self):
        return u'%s' % (self.desc_in)
    def save(self, force_insert=False, force_update=False):
        self.desc_in_en = self.get_comp_desc_in_en
        self.desc_in_es = self.get_comp_desc_in_es
        self.desc_mm_en = self.get_comp_desc_mm_en
        self.desc_mm_es = self.get_comp_desc_mm_es
        self.composicion_hash = self.get_composicionhash
        super(ComposicionCristal,self).save(force_insert,force_update)
    @models.permalink
    def get_absolute_url(self):
        return ('composicioncristal_detalle_l',[str(self.id)])
    @property
    def get_items_queryset(self):
        return self.itemcomposicion_set.order_by('posicion')
    @property
    def get_comp_desc_in_en(self):
        comp_desc_in_en = ''
        for item in self.get_items_queryset:
            comp_desc_in_en += item.desc_in_en
        return comp_desc_in_en
    @property
    def get_comp_desc_in_es(self):
        comp_desc_in_es = ''
        for item in self.get_items_queryset:
            comp_desc_in_es += item.desc_in_es
        return comp_desc_in_es
    @property
    def get_comp_desc_mm_en(self):
        comp_desc_mm_en = ''
        for item in self.get_items_queryset:
            comp_desc_mm_en += item.desc_mm_en
        return comp_desc_mm_en
    @property
    def get_comp_desc_mm_es(self):
        comp_desc_mm_es = ''
        for item in self.get_items_queryset:
            comp_desc_mm_es += item.desc_mm_es
        return comp_desc_mm_es
    @property
    def get_composicionhash(self):
        comp_hash = ''
        for item in self.get_items_queryset:
            comp_hash += item.hash
        return comp_hash
    @property
    def valid_compcristalhash(self):
        return ComposicionCristal.objects.filter(composicion_hash=self.get_composicionhash)
    @property
    def desc_in(self):
        return getself_trans(self)
    @property
    def desc_mm(self):
        return getself_trans(self)
 
class CristalTratamiento(models.Model):
    desc_en = models.CharField(_('Descripcion (Ing)'),max_length=150)
    desc_es = models.CharField(_('Descripcion (Esp)'),max_length=150)
    id_en = models.CharField(_('ID (Ing)'),max_length=100)
    id_es = models.CharField(_('ID (Esp)'),max_length=100)
 
    class Meta:
        app_label = 'catalogo'
        verbose_name = _('Tratamiento Cristal')
        verbose_name_plural = _('Tratamientos Cristal')
    def __unicode__(self):
        return u'%s' % (self.desc)
    @property
    def desc(self):
        return getself_trans(self)
 
class CristalColor(models.Model):
    id_en = models.CharField(_('ID (Ing)'),max_length=100)
    id_es = models.CharField(_('ID (Esp)'),max_length=100)
    desc_en = models.CharField(_('Descripcion (Ing)'),max_length=150)
    desc_es = models.CharField(_('Descripcion (Esp)'),max_length=150)
 
    class Meta:
        app_label = 'catalogo'
        verbose_name = _('Color Cristal')
        verbose_name_plural = _('Colores Cristal')
    def __unicode__(self):
        return u'%s' % (self.desc)
    @property
    def desc(self):
        return getself_trans(self)
 
class CristalAcabado(models.Model):
    id_en = models.CharField(_('ID (Ing)'),max_length=100)
    id_es = models.CharField(_('ID (Esp)'),max_length=100)
    desc_en = models.CharField(_('Descripcion (Ing)'),max_length=100)
    desc_es = models.CharField(_('Descripcion (Esp)'),max_length=100)
 
    class Meta:
        app_label = 'catalogo'
        verbose_name = _('Acabado Cristal')
        verbose_name_plural = _('Acabados Cristal')
    def __unicode__(self):
        return u'%s' % (self.desc)
    @property
    def desc(self):
        return getself_trans(self)
 
class CristalEspesor(models.Model):
    espesor_mm = MedidaModelField(verbose_name=_('espesor_mm'),unidad_alm='mm')
    espesor_inch = MedidaModelField(verbose_name=_('espesor_inch'),unidad_alm='in')
    espesor_inch_frac = models.CharField(_('Espesor_inch (Frac)'),max_length=100)
 
    class Meta:
        app_label = 'catalogo'
        verbose_name = _('Cristal Espesor')
        verbose_name_plural = _('Cristal Espesores')
    def __unicode__(self):
        return u'%s %s' % (self.espesor_inch_frac, self.espesor_mm)
    def cristal_es_mm(self):
        return u'%s' % (self.espesor_mm)
    def cristal_es_in(self):
        return u'%s' % (self.espesor_inch_frac)

class CristalColorEspesor(models.Model):
    color = models.ForeignKey(CristalColor)
    espesor = models.ForeignKey(CristalEspesor)
    cod_sap = models.CharField(verbose_name=_('CodigoSAP'), max_length=50)
    
    class Meta:
        app_label = 'catalogo'
        verbose_name = _('Cristal Color Espesor')
        verbose_name_plural = _('Cristal Colores Esperores')
    def __unicode__(self):
        return u'%s' % (self.desc)
    @property
    def desc(self):
        return u'%s %s' % (self.color,self.espesor)
 
class SeparadorTipo(models.Model):
    desc_en = models.CharField(_('Descripcion (Ing)'),max_length=150)
    desc_es = models.CharField(_('Descripcion (Esp)'),max_length=150)
 
    class Meta:
        app_label = 'catalogo'
        verbose_name = _('Tipo Separador')
        verbose_name_plural = _('Tipos Separador')
    def __unicode__(self):
        return u'%s' % (self.desc)
    @property
    def desc(self):
        return getself_trans(self)
 
class SeparadorMaterial(models.Model):
    separador_tipo = models.ForeignKey(SeparadorTipo, verbose_name=_('Tipo Separador'))
    desc_en = models.CharField(_('Descripcion (Ing)'),max_length=150)
    desc_es = models.CharField(_('Descripcion (Esp)'),max_length=150)
 
    class Meta:
        app_label = 'catalogo'
        verbose_name = _('Material Separador')
        verbose_name_plural = _('Materiales Separador')
    def __unicode__(self):
        return u'%s' % (self.desc)
    @property
    def desc(self):
        return getself_trans(self)
    
class SeparadorEspesor(models.Model):
    espesor_mm = MedidaModelField(verbose_name=_('espesor_mm'),unidad_alm='mm')
    espesor_inch = MedidaModelField(verbose_name=_('espesor_inch'),unidad_alm='in')
    espesor_inch_frac = models.CharField(_('Espesor_inch (Frac)'),max_length=100)
    
    class Meta:
        app_label = 'catalogo'
        verbose_name = _('Separador Espesor')
        verbose_name_plural = _('Separador Espesores')
    def __unicode__(self):
        return u'%s %s' % (self.espesor_inch_frac, self.espesor_mm.get_unicode())
    @property
    def sep_es_mm(self):
        return u'%s' % (self.espesor_mm)
    @property
    def sep_es_in(self):
        return u'%s' % (self.espesor_inch_frac)
 
class ItemComposicion(models.Model):
    posicion = models.IntegerField(verbose_name=_('Posicion'))
    compcristal = models.ForeignKey(ComposicionCristal,verbose_name=_('Composicion Cristal'))
    desc_in_en = models.CharField(_('Descripcion (Ing)'),max_length=150)
    desc_in_es = models.CharField(_('Descripcion (Ing)'),max_length=150)
    desc_mm_en = models.CharField(_('Descripcion (Esp)'),max_length=150)
    desc_mm_es = models.CharField(_('Descripcion (Esp)'),max_length=150)
    hash = models.CharField(_('Item Hash'),max_length=100)
    content_type = models.ForeignKey(ContentType,editable=False)
    item = generic.GenericForeignKey('content_type','id')
 
    class Meta:
        app_label = 'catalogo'
        verbose_name = _('Item Composicion')
        verbose_name_plural = _('Item Composicion')
    def __unicode__(self):
        return u'%s %s' % (self.posicion,self.desc_in)
    def save(self, force_insert=False, force_update=False):
        self.content_type = ContentType.objects.get_for_model(self)
        super(ItemComposicion,self).save(force_insert,force_update)
    @property
    def desc_in(self):
        return getself_trans(self)
    @property
    def desc_mm(self):
        return getself_trans(self)
    @classmethod
    def inst_item(cls,item_hash):
        id = item_hash[0]
        atr = []
        atr = item_hash[2:].split('-')
        if id == 'C':
            objeto = Cristal(tratamiento=CristalTratamiento.objects.get(id=int(atr[0])),color=CristalColor.objects.get(id=int(atr[1])),espesor=CristalEspesor.objects.get(id=int(atr[2])),acabado_cara_int=CristalAcabado.objects.get(id=int(atr[3])),acabado_cara_ext=CristalAcabado.objects.get(id=int(atr[4])))
        elif id == 'E':
            objeto = Entrecapa(material=EntrecapaMaterial.objects.get(id=int(atr[0])),espesor=SeparadorEspesor.objects.get(id=int(atr[1])))
        elif id == 'S':
            objeto = Separador(material=SeparadorMaterial.objects.get(id=int(atr[0])),espesor=SeparadorEspesor.objects.get(id=int(atr[1])))
        return objeto
 
class Cristal(ItemComposicion):
    tratamiento = models.ForeignKey(CristalTratamiento,verbose_name=_('Tratamiento'))
    color = models.ForeignKey(CristalColor,verbose_name=_('Color'))
    espesor = models.ForeignKey(CristalEspesor, verbose_name=_('Espesor'))
    acabado_cara_int = models.ForeignKey(CristalAcabado,verbose_name=_('Acbd. Cara Int.'),related_name='acabado_cara_interna')
    acabado_cara_ext = models.ForeignKey(CristalAcabado,verbose_name=_('Acbd. Cara Ext.'),related_name='acabado_cara_externa')
 
    class Meta:
        app_label = 'catalogo'
        verbose_name = _('Cristal')
        verbose_name_plural = _('Cristal')
    def __unicode__(self):
        return u'%s' % (self.desc_in_en)
    def save(self, force_insert=False, force_update=False):
        self.desc_in_en = self.get_desc_in_en
        self.desc_in_es = self.get_desc_in_es
        self.desc_mm_en = self.get_desc_mm_en
        self.desc_mm_es = self.get_desc_mm_es
        self.hash = self.get_hash
        super(Cristal,self).save(force_insert,force_update)
    @property
    def get_desc_in_en(self):
        return u'%s %s %s %s %s' % (self.espesor.cristal_es_in(), self.tratamiento.id_en, self.color.id_en, self.acabado_cara_int.id_en, self.acabado_cara_ext.id_en)
    @property
    def get_desc_in_es(self):
        return u'%s %s %s %s %s' % (self.espesor.cristal_es_in(), self.tratamiento.id_es, self.color.id_es, self.acabado_cara_int.id_es, self.acabado_cara_ext.id_es)
    @property
    def get_desc_mm_en(self):
        return u'%s %s %s %s %s' % (self.espesor.cristal_es_mm(), self.tratamiento.id_en, self.color.id_en, self.acabado_cara_int.id_en, self.acabado_cara_ext.id_en)
    @property
    def get_desc_mm_es(self):
        return u'%s %s %s %s %s' % (self.espesor.cristal_es_mm(), self.tratamiento.id_es, self.color.id_es, self.acabado_cara_int.id_es, self.acabado_cara_ext.id_es)
    @property
    def get_hash(self):
        return u'C-%s-%s-%s-%s-%s' % (self.espesor.id, self.tratamiento.id, self.color.id, self.acabado_cara_int.id, self.acabado_cara_ext.id)
 
 
class Separador(ItemComposicion):
    material = models.ForeignKey(SeparadorMaterial,verbose_name=_('Material'))
    espesor = models.ForeignKey(SeparadorEspesor, verbose_name=_('Espesor'))
 
    class Meta:
        app_label = 'catalogo'
        verbose_name = _('Separador')
        verbose_name_plural = _('Separador')
    def __unicode__(self):
        return u'(%s-%s)' % (self.material,self.espesor)
    def save(self, force_insert=False, force_update=False):
        self.desc_in_en = self.get_desc_in_en
        self.desc_in_es = self.get_desc_in_es
        self.desc_mm_en = self.get_desc_mm_en
        self.desc_mm_es = self.get_desc_mm_es
        self.hash = self.get_hash
        super(Separador,self).save(force_insert,force_update)
    @property
    def get_desc_in_en(self):
        return u' + %s %s + ' % (self.espesor.sep_es_in, self.material.desc)
    @property
    def get_desc_in_es(self):
        return u' + %s %s + ' % (self.espesor.sep_es_in, self.material.desc)
    @property
    def get_desc_mm_en(self):
        return u' + %s %s + ' % (self.espesor.sep_es_mm, self.material.desc)
    @property
    def get_desc_mm_es(self):
        return u' + %s %s + ' % (self.espesor.sep_es_mm, self.material.desc)
    @property
    def get_hash(self):
        return u'+S-%s-%s+' % (self.espesor.id, self.material.id)
    

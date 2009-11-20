from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.cache import cache
from exceptions import SistemaMedidaNoExiste, TipoUnidadNoExiste, UnidadMedidaNoExiste, ConversionNoExiste
from base.helpers import getself_trans

__all__ = [
    "SistemaMedida",
    "TipoUnidad",
    "UnidadMedida",
    "ConversionManager",
    "Conversion",
    "UnidadTipoSistema",
]

class SistemaMedida(models.Model):
    ref = models.CharField(_('Referencia'),max_length=5)
    unidades_tipo = models.ManyToManyField('TipoUnidad',through='UnidadTipoSistema',null=True,blank=True)
    abrev_en = models.CharField(_('Abreviacion (Ing)'),max_length=5)
    abrev_es = models.CharField(_('Abreviacion (Esp)'),max_length=5)
    nombre_en = models.CharField(_('Nombre (Ing)'),max_length=150)
    nombre_es = models.CharField(_('Nombre (Esp)'),max_length=150)
    @property
    def abrev(self):
        return getself_trans(self)
    @property
    def nombre(self):
        return getself_trans(self)
    def __unicode__(self):
        return u'%s' % self.nombre
    @classmethod
    def buscar(cls,ref):
        try:
            return cls.objects.get(ref = ref)
        except:
            raise SistemaMedidaNoExiste(ref)
    def u_tipo(self,tipo):
        u = cache.get('UnidadTipoSistema S-%i T-%i'%(self.id,tipo.id))
        if not u:
            u = self.unidadtiposistema_set.get(tipo=tipo).unidad
            cache.add('UnidadTipoSistema S-%i T-%i'%(self.id,tipo.id),u)
        return u
    class Meta:
        verbose_name = _('Sistema Medida')
        verbose_name_plural = _('Sistemas Medida')
        ordering = ['ref']

class TipoUnidad(models.Model):
    ref = models.CharField(_('Referencia'),max_length=5)
    abrev_en = models.CharField(_('Abreviacion (Ing)'),max_length=5)
    abrev_es = models.CharField(_('Abreviacion (Esp)'),max_length=5)
    nombre_en = models.CharField(_('Nombre (Ing)'),max_length=150)
    nombre_es = models.CharField(_('Nombre (Esp)'),max_length=150)
    @property
    def abrev(self):
        return getself_trans(self)
    @property
    def nombre(self):
        return getself_trans(self)
    def __unicode__(self):
        return u'%s' % self.nombre
    @classmethod
    def buscar(cls,ref):
        try:
            return cls.objects.get(ref=ref)
        except:
            raise TipoUnidadNoExiste(ref)
    class Meta:
        verbose_name = _('Tipo Unidad')
        verbose_name_plural = _('Tipos Unidad')
        ordering = ['ref']

class UnidadMedida(models.Model):
    ref = models.CharField(_('Referencia'),max_length=5)
    abrev_en = models.CharField(_('Abreviacion (Ing)'),max_length=5)
    abrev_es = models.CharField(_('Abreviacion (Esp)'),max_length=5)
    nombre_en = models.CharField(_('Nombre (Ing)'),max_length=150)
    nombre_es = models.CharField(_('Nombre (Esp)'),max_length=150)
    @property
    def abrev(self):
        return getself_trans(self)
    @property
    def nombre(self):
        return getself_trans(self)
    sistema = models.ForeignKey(SistemaMedida,related_name='unidades',verbose_name=_('Sistema'))
    tipo = models.ForeignKey(TipoUnidad,related_name='unidades',verbose_name=_('Tipo Unidad'))
    conversiones = models.ManyToManyField('self',verbose_name=_('Conversiones'),through='Conversion',symmetrical=False)
    #objects = UnidadMedidaManager()
    def __unicode__(self):
        return u'%s' % self.abrev
    @classmethod
    def buscar(cls,ref):
        #try:
        return cls.objects.get(ref = ref)
        #except:
        #    raise UnidadMedidaNoExiste(ref)
    @classmethod
    def buscar_tipo(cls,tipo):
        if isinstance(tipo,TipoUnidad):
            return cls.objects.filter(tipo=tipo)
        else:
            return cls.objects.filter(tipo__ref=tipo)
    def unidad_sistema(self,sistema):
        if self.sistema == sistema: return self
        else: return self.unidadtiposistema_set.get(tipo=self.tipo,sistema=sistema)
    class Meta:
        verbose_name = _('Unidad Medida')
        verbose_name_plural = _('Unidades Medida')
        ordering = ['sistema','tipo','ref']

class ConversionManager(models.Manager):
    def factor(self,o,d):
        if o == d: return decimal.Decimal(1)
        factor = cache.get('Conv %i->%i'%(o.id,d.id))
        if not factor:
            factor = self.get_query_set.get(unidad_origen=o,unidad_destino=d).factor
            cache.add('Conv %i->%i'%(o.id,d.id),factor)
        if not factor:
            raise ConversionNoExiste(o,d)
        return factor

class Conversion(models.Model):
    unidad_origen = models.ForeignKey(UnidadMedida,related_name='u_origen',verbose_name=_('Unidad Origen'))
    unidad_destino = models.ForeignKey(UnidadMedida,related_name='u_destino',verbose_name=_('Unidad Destino'))
    factor = models.DecimalField(max_digits=30,decimal_places=10,default=0)
    objects = ConversionManager()
    @property
    def sistema_origen(self):
        return self.unidad_origen.sistema
    @property
    def sistema_destino(self):
        return self.unidad_destino.sistema
    @classmethod
    def buscar_factor(cls,o,d):
        factor = cache.get('Con %i->%i'%(o.id,d.id))
        if not factor:
            factor = cls.objects.get(unidad_origen=o,unidad_destino=d).factor
            cache.add('Conv %i->%i'%(o.id,d.id),factor)
        return factor
    def __unicode__(self):
        return u'%s -> %s' % (self.unidad_origen,self.unidad_destino)
    def save(self, force_insert=False, force_update=False):
        if self.unidad_origen == self.unidad_destino:
            #raise exceptions.ValidationError(_('Ha selecionado la misma'))
            return
        else:
            super(Conversion,self).save(force_insert,force_update)
    class Meta:
        verbose_name = _('Conversion')
        verbose_name_plural = _('Conversiones')
        ordering = ['unidad_origen','unidad_destino']

class UnidadTipoSistema(models.Model):
    sistema = models.ForeignKey(SistemaMedida,verbose_name=_('Sistema'))
    tipo = models.ForeignKey(TipoUnidad,verbose_name=_('Tipo'))
    unidad = models.ForeignKey(UnidadMedida,verbose_name=_('Unidad'))
    def __unicode__(self):
        return u'%s' % self.unidad
    class Meta:
        verbose_name=_('Unidad Tipo Sistema')
        verbose_name_plural = _('Unidades Tipo Sistema')
        unique_together = (('sistema','tipo'),)
        ordering = ['sistema','tipo','unidad']


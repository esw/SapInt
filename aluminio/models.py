from django.db import models
from string import zfill

class Acabado(models.Model):
    nombre = models.CharField('Nombre',max_length=50)
    class Meta:
        verbose_name = 'Acabado'
        verbose_name_plural = 'Acabados'
        ordering = ['nombre']
        unique_together = ('nombre',)
    def __unicode__(self):
        return u'%s' % self.nombre
    
class Aleacion(models.Model):
    codigo = models.CharField('Codigo',max_length=10)
    class Meta:
        verbose_name = 'Aleacion'
        verbose_name_plural = 'Aleaciones'
        ordering = ['codigo']
        unique_together = ('codigo',)
    def __unicode__(self):
        return u'%s' % self.codigo
    
class Temple(models.Model):
    codigo = models.CharField('Codigo',max_length=5)
    class Meta:
        verbose_name = 'Temple'
        verbose_name_plural = 'Temples'
        ordering = ['codigo']
        unique_together = ('codigo',)
    def __unicode__(self):
        return u'%s' % self.codigo

class Referencia(models.Model):
    nombre = models.CharField('Nombre',max_length=20)
    aleacion_std = models.ForeignKey(Aleacion,verbose_name='Aleacion Estandard', null=True, blank=True)
    temple_std = models.ForeignKey(Temple,verbose_name='Temple Estandard', null=True, blank=True)
    peso_lineal = models.FloatField('Peso Lineal (kg/m)')
    perim_exp = models.FloatField('Perimetro Expuesto', null=True, blank=True)
    perim_total = models.FloatField('Perimetro Total', null=True, blank=True)
    class Meta:
        verbose_name = 'Referencia'
        verbose_name_plural = 'Referencias'
        ordering = ['nombre']
        unique_together = ('nombre',)
    def __unicode__(self):
        return u'%s' % self.nombre

SISTEMAS_LEGACY_ALM = (
    ('Ep','Epics'),
    ('ES','EnergiaSolar'),
)

class RefLegacy(models.Model):
    sistema = models.CharField('sistema',choices=SISTEMAS_LEGACY_ALM,max_length=3)
    ref_legacy = models.CharField('ref legacy',max_length=30)
    referencia = models.ForeignKey(Referencia,verbose_name='referencia')
    class Meta:
        verbose_name = 'Referencia Legacy'
        verbose_name_plural = 'Referencias Legacy'
        ordering = ['ref_legacy']
        unique_together = ('sistema','ref_legacy')
    def __unicode__(self):
        return u'%s %s' % (self.get_sistema_display(),self.ref_legacy)

TIPOS_MAT_SAP = (
    ('FERT','Prod Terminado'),
    ('HALB','Prod Semielaborado'),
)

class SapAluminio(models.Model):
    referencia = models.ForeignKey(Referencia,verbose_name='referencia')
    aleacion = models.ForeignKey(Aleacion)
    temple = models.ForeignKey(Temple)
    acabado = models.ForeignKey(Acabado)
    largo_mm = models.IntegerField('Largo (mm)')
    tipo_mat = models.CharField('Tipo Material',max_length=6, choices=TIPOS_MAT_SAP, default='FERT')
    class Meta:
        verbose_name = 'Aluminio MatSAP'
        verbose_name_plural = 'Aluminios MatSAP'
        ordering = ['referencia','aleacion','temple','acabado','largo_mm']
        unique_together = ('referencia','aleacion','temple','acabado','largo_mm')
    def __unicode__(self):
        return self.desc
    @property
    def desc(self):
        return u'%s %s %s%s %s' % (self.referencia, self.acabado, self.aleacion, self.temple, self.largo_mm)
    @property
    def len_desc(self):
        return len(self.desc)
    @property
    def cod_sap(self):
        return u'A%s%s%s%s%s' % (
            str(self.referencia.id).zfill(5),
            str(self.acabado.id).zfill(3),
            str(self.aleacion.id).zfill(2),
            str(self.temple.id).zfill(2),
            str(self.largo_mm).zfill(5)
            )
    
    
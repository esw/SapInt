from django.db import models

class SiggerMat(models.Model):
    codigo = models.CharField('Codigo', max_length=50)
    desc = models.CharField('Descripcion', max_length=50)
    saldo = models.FloatField('Saldo', null=True, blank=True)
    costo_u = models.FloatField('Costo', null=True, blank=True)
    cod_sap = models.CharField('Codigo SAP', max_length=50, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Material Sigger'
        verbose_name_plural = 'Materiales Sigger'
        ordering = ['desc',]
        unique_together = ('codigo',)
    def __unicode__(self):
        return self.desc


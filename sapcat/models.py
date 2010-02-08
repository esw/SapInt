from django.db import models

class Centro(models.Model):
    nombre = models.CharField(max_length=50)
    cod_sap = models.CharField(max_length=10)
    class Meta:
        verbose_name = 'Centro'
        verbose_name_plural = 'Centros'
        ordering = ['nombre']
        unique_together = ('nombre',)
    def __unicode__(self):
        return u'%s' % self.nombre

class TipoMaterial(models.Model):
    nombre = models.CharField(max_length=50)
    class Meta:
        verbose_name = 'Tipo Material'
        verbose_name_plural = 'Tipos Materiales'
        ordering = ['nombre']
        unique_together = ('nombre',)
    def __unicode__(self):
        return u'%s' % self.nombre


class ParamsMaterial(models.Model):
    tipo_mat = models.ForeignKey(TipoMaterial)
    indt_sect = models.CharField('Sector Industria',max_length=10, null=True, blank=True)
    base_uom = models.CharField('Unidad Medida Base', max_length=10, null=True, blank=True)
    matl_grp = models.CharField('Grupo Articulo', max_length=10, null=True, blank=True)
    division = models.CharField('Sector', max_length=10, null=True, blank=True)
    gen_item_cat_grp = models.CharField('Grupo Tipo de Pos General', max_length=10, null=True, blank=True)
    class Meta:
        verbose_name = 'Parametros Material'
        verbose_name_plural = 'Parametros Materiales'
        ordering = ['tipo_mat']
        unique_together = ('tipo_mat',)
    def __unicode__(self):
        return u'Params %s' % self.tipo_mat
    

#class ParamsMaterialCentro(models.Model):
#    centro = models.ForeignKey(Centro)
#    tipo_mat = models.ForeignKey(TipoMaterial)
#    clasif_fiscal = models.CharField(verbose_name='Clasificacion Fiscal', max_length=10, null=True, blank=True)
#    cat_val = models.CharField(verbose_name='Categoria de Valoracion', max_length=10, null=True, blank=True)
#    centro_benef = models.CharField(verbose_name='Centro de Beneficio', max_length=10, null=True, blank=True)
#    class Meta:
#        verbose_name = 'Parametros Material Centro'
#        verbose_name_plural = 'Parametros Materiales Centros'
#        ordering = ['centro','tipo_mat']
#        unique_together = ('centro','tipo_mat',)
#    def __unicode__(self):
#        return u'Params %s %s' % (self.centro,self.tipo_mat)
    
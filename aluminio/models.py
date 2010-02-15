from django.db import models
from django.db.models.aggregates import Sum
from string import zfill
from decimal import Decimal
from math import floor
from django.core.exceptions import ObjectDoesNotExist

SCRAP_COD_SAP_MAT = '20000005'
PRIMER_CONS_CALC = 48.77
PRIMER_COD_SAP_MAT = '30000719'
DCLEAR_COD_SAP_MAT = '30006608'
DCLEAR_CONS_CALC = 32.51


class TipoAcabado(models.Model):
    nombre = models.CharField('Nombre',max_length=30)
    cons_calc = models.FloatField('Constante Calculo (m2/gal)', null=True, blank=True)
    primer = models.BooleanField('Utiliza Primer', default=False)
    d_clear = models.BooleanField('Utiliza Duranar Clear', default=False)
    prod_scheduler = models.CharField('Prod Scheduler', max_length=30, null=True, blank=True)
    texto_lista = models.CharField('Texto Lista Material', max_length=40, null=True, blank=True)
    class Meta:
        verbose_name = 'Tipo Acabado'
        verbose_name_plural = 'Tipos Acabados'
        ordering = ['nombre']
        unique_together = ('nombre',)
    def __unicode__(self):
        return u'%s' % self.nombre
    def grupo_hr(self):
        if self.prod_scheduler=='ALA':
            return '10000000'
        if self.prod_scheduler=='ALC':
            return '10000001'
        if self.prod_scheduler=='ALP':
            return '10000002'
        return '10000001'

class GrupoValoracion(models.Model):
    codigo = models.CharField('Codigo', max_length=30)
    valor_total = models.FloatField('Valor Total', blank=True, null=True)
    peso_total_kg = models.FloatField('Peso Total (kg)', blank=True, null=True)
    class Meta:
        verbose_name = 'Grupo Valoracion'
        verbose_name_plural = 'Grupos Valoracion'
        ordering = ['codigo']
        unique_together = ('codigo',)

class Acabado(models.Model):
    nombre = models.CharField('Nombre',max_length=50)
    cod_sap_mat = models.CharField('Codigo Material SAP', max_length=25, null=True, blank=True)
    tipo = models.ForeignKey(TipoAcabado, null=True, blank=True)
    cod_epics = models.CharField('Codigo Epics', max_length=50, null=True, blank=True)
    prod_alutions = models.BooleanField('Produccion Alutions',default=True)
    grupo_mat = models.CharField('GrupoMat (Ventas)', max_length=10, null=True, blank=True)
    class Meta:
        verbose_name = 'Acabado'
        verbose_name_plural = 'Acabados'
        ordering = ['nombre']
        unique_together = ('nombre',)
    def __unicode__(self):
        return u'%s' % self.nombre
    @property
    def prod_scheduler(self):
        if self.tipo is not None: return self.tipo.prod_scheduler
        return None
    @property
    def texto_lista(self):
        return self.tipo.texto_lista
    @property
    def grupo_hr(self):
        return self.tipo.grupo_hr()
    
class Aleacion(models.Model):
    codigo = models.CharField('Codigo',max_length=10)
    especial = models.BooleanField(default=True)
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
    perim_exp = models.FloatField('Perimetro Expuesto (m)', null=True, blank=True)
    perim_total = models.FloatField('Perimetro Total (m)', null=True, blank=True)
    unbw = models.BooleanField('UNBW', default=False)
    class Meta:
        verbose_name = 'Referencia'
        verbose_name_plural = 'Referencias'
        ordering = ['nombre']
        unique_together = ('nombre',)
    def __unicode__(self):
        return u'%s' % self.nombre
    def save(self, *args, **kwargs):
        self.peso_lineal = round(self.peso_lineal,3)
        super(Referencia, self).save(*args, **kwargs)

TIPO_NAC = 'NAC'
TIPO_IMP = 'IMP'
TIPO_CHI = 'CHI'
TIPOS_TOCHO = (
    (TIPO_NAC,'Nacional'),
    (TIPO_IMP,'Importado'),
    (TIPO_CHI,'Chino'),
    )

class Tocho(models.Model):
    tipo = models.CharField('Tipo Tocho', choices=TIPOS_TOCHO, max_length=30)
    aleacion = models.ForeignKey(Aleacion)
    cod_sap = models.CharField('Cod_Sap', max_length=40)
    class Meta:
        unique_together = (('tipo','aleacion'),('cod_sap',),)
    def __unicode__(self):
        return u'%s %s' % (self.tipo,self.aleacion)

class UbicacionSap(models.Model):
    codigo = models.CharField('Codigo', max_length=30)
    area = models.CharField('Area Almacenamiento', max_length=30, null=True, blank=True)
    class Meta:
        verbose_name = 'UbicacionSap'
        verbose_name_plural = 'UbicacionesSap'
        unique_together = ('codigo',)
    def __unicode__(self):
        return u'%s' % self.codigo

SIST_ANT = (
    ('WMS','WMS'),
    ('EPICS','EPICS'),
    )

class ReferenciaSAnt(models.Model):
    sistema = models.CharField('Sistema', max_length=50, choices=SIST_ANT)
    ref_ant = models.CharField('RefAnt',max_length=30)
    peso_lineal = models.FloatField('Peso Lineal (kg/m)', null=True, blank=True)
    referencia = models.ForeignKey(Referencia,verbose_name='referencia')
    class Meta:
        verbose_name = 'Referencia SistAnt'
        verbose_name_plural = 'Referencias SistAnt'
        ordering = ['sistema','ref_ant']
        unique_together = ('sistema','ref_ant')
    def __unicode__(self):
        return u'%s %s' % (self.sistema,self.ref_ant)

class AcabadoSAnt(models.Model):
    sistema = models.CharField('Sistema', max_length=50, choices=SIST_ANT)
    acab_ant = models.CharField('Codigo Anterior', max_length=150)
    acabado = models.ForeignKey(Acabado, verbose_name='Acabado')
    class Meta:
        verbose_name = 'Acabado SistAnt'
        verbose_name_plural = 'Acabados SistAnt'
        ordering = ['sistema', 'acab_ant']
        unique_together = ('sistema', 'acab_ant')
    def __unicode__(self):
        return u'%s %s' % (self.sistema, self.acab_ant)

class UbicacionSAnt(models.Model):
    sistema = models.CharField('Sistema', max_length=50, choices=SIST_ANT)
    ubicacion_ant = models.CharField('Ubicacion Anterior', max_length=50)
    ubicacion_sap = models.ForeignKey(UbicacionSap, verbose_name='Ubicacion SAP')
    class Meta:
        verbose_name = 'Ubicacion SistAnt'
        verbose_name_plural = 'Ubicaciones SistAnt'
        ordering = ['sistema','ubicacion_ant']
        unique_together = ('sistema','ubicacion_ant')
    def __unicode__(self):
        return u'%s %s' % (self.sistema, self.ubicacion_ant)
  
TIPOS_MAT_SAP = (
    ('FERT', 'FERT'),
    ('HALB', 'HALB'),
    ('UNBW', 'UNBW'),
)

def check_tipo_by_cod(cod_sap):
    if cod_sap[0] == '6': return 'UNBW'
    else: return 'FERT'

COD_SAP_FERT_INIT = 10015524
COD_SAP_UNBW_INIT = 60000000

CODS_SAP_INIT = {
    'FERT': COD_SAP_FERT_INIT,
    'UNBW': COD_SAP_UNBW_INIT,
}

class SapAluminioManager(models.Manager):
    def sin_cargar(self,tipo_mat=None):
        if tipo_mat is None: return self.filter(cargado=False)
        else: return self.filter(cargado=False, tipo_mat=tipo_mat)
    def cargados(self,tipo_mat=None):
        if tipo_mat is None: return self.filter(cargado=True)
        else: return self.filter(cargado=True, tipo_mat=tipo_mat)
    def next_cod(self,tipo_mat='FERT'):
        val = self.cargados(tipo_mat=tipo_mat).aggregate(models.Max('cod_sap'))['cod_sap__max']
        if val is not None: i = int(val)
        else: i = CODS_SAP_INIT[tipo_mat]
        return i + 1
    def next_cod_fert(self):
        return self.next_cod(tipo_mat='FERT')
    def next_cod_unbw(self):
        return self.next_cod(tipo_mat='UNBW')

class SapAluminio(models.Model):
    cod_sap = models.CharField('CodigoSAP',max_length=50,null=True,blank=True)
    referencia = models.ForeignKey(Referencia,verbose_name='referencia')
    aleacion = models.ForeignKey(Aleacion)
    temple = models.ForeignKey(Temple)
    acabado = models.ForeignKey(Acabado)
    largo_mm = models.IntegerField('Largo (mm)')
    tipo_mat = models.CharField('Tipo Material',max_length=6, choices=TIPOS_MAT_SAP, default='FERT')
    cargado = models.BooleanField('Cargado a SAP', default=False)
    
    objects = SapAluminioManager()
    
    class Meta:
        verbose_name = 'Aluminio MatSAP'
        verbose_name_plural = 'Aluminios MatSAP'
        ordering = ['id','cod_sap','referencia','aleacion','temple','acabado','largo_mm']
        unique_together = (('referencia','aleacion','temple','acabado','largo_mm','tipo_mat'),('cod_sap',))
    def save(self, *args, **kwargs):
        #if self.grupo_val is None and self.acabado.grupo_val is not None:
        #    self.grupo_val = self.acabado.grupo_val
        if self.cod_sap is not None: self.cod_sap = zfill(self.cod_sap,18)
        super(SapAluminio, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.desc
    @property
    def cod_sap_zfill(self):
        return zfill(self.cod_sap,18)
    @property
    def desc(self):
        return u'%s %s %s%s %s' % (self.referencia, self.acabado, self.aleacion, self.temple, self.largo_mm)
    @property
    def len_desc(self):
        return len(self.desc)
    @property
    def cod_epics_acabado(self):
        return self.acabado.cod_epics
    @property
    def cod_sap_acabado(self):
        return self.acabado.cod_sap_mat
    @property
    def grupo_mat(self):
        return self.acabado.grupo_mat
    @property
    def peso_lineal(self):
        return self.referencia.peso_lineal
    @property    
    def peso_lineal_1000(self):
        return int(round(self.peso_kg*1000))
    @property
    def peso_lineal_1000_malo(self):
        return int(floor(self.peso_kg*1000))
    @property
    def peso_kg(self):
        return round((float(self.largo_mm) / 1000) * self.referencia.peso_lineal,3)
    @property
    def peso_kg_str(self):
        return str(self.peso_kg).replace('.',',')
    @property
    def perim_exp(self):
        return self.referencia.perim_exp
    @property
    def area_exp(self):
        perim_exp = self.referencia.perim_exp
        if perim_exp is not None: return (self.largo_mm / 1000) * perim_exp
        return None
    @property
    def prod_scheduler(self):
        return self.acabado.prod_scheduler
    @property
    def texto_lista(self):
        return self.acabado.texto_lista
    @property
    def pintado(self):
        if self.acabado.tipo.cons_calc == 0: return False
        else: return True
    @property
    def primer(self):
        return self.acabado.tipo.primer
    @property
    def d_clear(self):
        return self.acabado.tipo.d_clear
    @property
    def cod_acabado(self):
        return self.acabado.cod_sap_mat
    @property
    def grupo_hr(self):
        return self.acabado.grupo_hr
    def get_cod_tocho(self, tipo):
        try:
            return Tocho.objects.get(aleacion=self.aleacion,tipo=tipo).cod_sap
        except ObjectDoesNotExist:
            return None
    @property
    def cod_primer(self):
        return PRIMER_COD_SAP_MAT
    @property
    def cod_dclear(self):
        return DCLEAR_COD_SAP_MAT
    @property
    def cant_acabado(self):
        area_exp = self.area_exp
        cons_calc = self.acabado.tipo.cons_calc
        if area_exp and cons_calc: return round(area_exp / cons_calc, 3)
        return None
    @property
    def cant_primer(self):
        if not self.acabado.tipo.primer: return 0
        area_exp = self.area_exp
        cons_calc = PRIMER_CONS_CALC
        if area_exp and cons_calc: return round(area_exp / cons_calc, 3)
        return None
    @property
    def cant_dclear(self):
        if not self.acabado.tipo.d_clear: return 0
        area_exp = self.area_exp
        cons_calc = DCLEAR_CONS_CALC
        if area_exp and cons_calc: return round(area_exp / cons_calc, 3)
        return None
    @property
    def costo_kg(self):
        return 1
    def row_lista(self):
        return [
            self.cod_sap,
            self.referencia,
            self.aleacion,
            self.temple,
            self.acabado,
            self.largo_mm,
            self.tipo_mat,
            self.peso_lineal,
            self.peso_kg,
            self.peso_lineal_1000
        ]
    
class SaldoWms(models.Model):
    codigo = models.CharField(max_length=50)
    referencia = models.ForeignKey(Referencia)
    aleacion = models.ForeignKey(Aleacion)
    temple = models.ForeignKey(Temple)
    acabado = models.ForeignKey(Acabado)
    largo_mm = models.IntegerField()
    ubicacion = models.ForeignKey(UbicacionSap)
    cant = models.IntegerField('Cantidad')
    proyecto = models.CharField(max_length=50)
    reserva = models.CharField(max_length=50, blank=True, null=True)
    tipo_mat = models.CharField('Tipo Material', max_length=6, choices=TIPOS_MAT_SAP, default='FERT')
    grupo_val = models.ForeignKey(GrupoValoracion, null=True, blank=True)
    sapalum = models.ForeignKey(SapAluminio, null=True, blank=True)
    precio = models.IntegerField('Precio',null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Saldos WMS'
        ordering = ['tipo_mat','referencia','aleacion','temple','acabado','largo_mm','ubicacion','proyecto','reserva']
        #unique_together = ('referencia','aleacion','temple','acabado','largo_mm','ubicacion','proyecto','reserva','tipo_mat','codigo')
    def save(self, *args, **kwargs):
        #if self.grupo_val is None and self.acabado.grupo_val is not None:
        #    self.grupo_val = self.acabado.grupo_val
        super(SaldoWms, self).save(*args, **kwargs)
    @property
    def cod_sap(self):
        return zfill(self.sapalum.cod_sap,18)
    @property
    def peso_lineal(self):
        return self.referencia.peso_lineal
    @property
    def peso_kg(self):
        #if sapalum is not None: return self.sapalum.peso_kg
        return round((Decimal(self.largo_mm) / 1000 * Decimal(str(self.peso_lineal))),3)
    @property
    def peso_total_kg(self):
        return self.peso_kg * self.cant
    @property
    def area_ubi(self):
        return self.ubicacion.area
    @property
    def ubicacion_cod(self):
        return self.ubicacion.codigo
    @staticmethod
    def row_head_saldo():
        row = []
        row.append('Codigo')
        row.append('Referencia')
        row.append('Aleacion')
        row.append('Temple')
        row.append('Acabado')
        row.append('Largo MM')
        row.append('Cantidad')
        row.append('Pesolineal (KG/M)')
        row.append('Peso KG (Unidad)')
        row.append('Peso KG Total')
        row.append('Ubicacion')
        #row.append('Proyecto')
        row.append('Reserva')
        row.append('Precio')
        row.append('Tipo Mat')
        row.append('Codigo SAP')
        return row
    def row_saldo(self):
        return [
            self.codigo,
            self.referencia,
            self.aleacion,
            self.temple,
            self.acabado,
            self.largo_mm,
            self.cant,
            self.peso_lineal,
            self.peso_kg,
            self.peso_total_kg,
            self.ubicacion,
            #self.proyecto,
            self.reserva,
            self.precio,
            self.tipo_mat,
            self.cod_sap
        ]
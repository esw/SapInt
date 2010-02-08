
import logging

from django.core.management.base import NoArgsCommand, BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from settings import ARCH_IMP_ROOT, IMP_REFS

from aluminio.imp_exp import *

ARCH_51_1 = '51_1_Inventario.txt'
ARCH_STOCK = 'Plantilla Stock WM Aluminio.txt'
ARCH_SALDOS = 'Saldos Formato SAP.txt'

DICT_ROW_51_1 = [
    { 'header':'DT_POSTG', 'tipo':'T', 'valor':'03.02.2009', 'desc':'Fecha Cargue' },
    { 'header':'DT_DOC', 'tipo':'T', 'valor':'03.02.2009', 'desc':'Fecha Cargue' },
    { 'header':'CAB_TEXT', 'tipo':'T', 'valor':'Cargue Inicial', 'desc':'Texto' },
    { 'header':'LONG_TEXT', 'tipo':'P', 'valor':'cons', 'desc':'Consecutivo' },
    { 'header':'MVT_TYPE', 'tipo':'T', 'valor':'561', 'desc':'Tipo de Movimiento' },
    { 'header':'MAT_NUM', 'tipo':'C', 'valor':'cod_sap', 'desc':'Codigo SAP' },
    { 'header':'STK_QTY', 'tipo':'C', 'valor':'peso_total_kg', 'desc':'Cantidad Kilos' },
    { 'header':'STK_UOM', 'tipo':'T', 'valor':'KG', 'desc':'Unidad' },
    { 'header':'PLANT', 'tipo':'T', 'valor':'1100', 'desc':'Centro' },
    { 'header':'SLOC', 'tipo':'T', 'valor':'1130', 'desc':'' },
    { 'header':'IMP_EXT', 'tipo':'C', 'valor':'precio', 'desc':'Importe','UNBW':False },
]
    
def get_rows_51_1(saldo, cons):
    return [get_row_from_dicts(DICT_ROW_51_1,saldo,cons=cons),]

DICT_ROW_STOCK = [
    { 'header':'LGNUM', 'tipo':'T', 'valor':'CAE', 'desc':'' },
    { 'header':'BWLVS', 'tipo':'T', 'valor':'999', 'desc':'' },
    { 'header':'MATNR', 'tipo':'C', 'valor':'cod_sap', 'desc':'Codigo Material' },
    { 'header':'ANFME', 'tipo':'C', 'valor':'cant', 'desc':'Cantidad' },
    { 'header':'ALTME', 'tipo':'T', 'valor':'UN', 'desc':'Unidad' },
    { 'header':'WERKS', 'tipo':'T', 'valor':'1100', 'desc':'' },
    { 'header':'LGORT', 'tipo':'T', 'valor':'1130', 'desc':'' },
    { 'header':'SQUIT', 'tipo':'T', 'valor':'X', 'desc':'' },
    { 'header':'VLTYP', 'tipo':'T', 'valor':'998', 'desc':'' },
    { 'header':'VLBER', 'tipo':'T', 'valor':'001', 'desc':'' },
    { 'header':'VLPLA', 'tipo':'T', 'valor':'AUFNAHME', 'desc':'' },
    { 'header':'NLTYP', 'tipo':'T', 'valor':'AE1', 'desc':'Bodega' },
    { 'header':'NLBER', 'tipo':'C', 'valor':'area_ubi', 'desc':'Area Ubicacion' },
    { 'header':'NLPLA', 'tipo':'C', 'valor':'ubicacion_cod', 'desc':'Ubicacion' },
    #{ 'header':'', 'tipo':'T', 'valor':'', 'desc':'' },
]

def get_rows_STOCK(saldo):
    return [get_row_from_dicts(DICT_ROW_STOCK,saldo),]

def exp_saldos_sap():
    wout_1 = get_writer(ARCH_51_1)
    wout_2 = get_writer(ARCH_STOCK)
    wout_3 = get_writer(ARCH_SALDOS)
    
    wout_1.writerow(get_headers_from_dicts(DICT_ROW_51_1))
    wout_2.writerow(get_headers_from_dicts(DICT_ROW_STOCK))
    #wout_3.writerow([SaldoWms.row_head_saldo,])
    
    cons = 0
    
    for saldo in SaldoWms.objects.all():
        cons = cons + 1
        #if saldo.sapalum.cod_sap is None:
        #if saldo.tipo_mat == 'FERT':
        #    saldo.cod_sap = zfill(cod_fert,18)
        #    cod_fert = cod_fert + 1
        #elif s_alum.tipo_mat == 'UNBW':
        #    saldo.cod_sap = zfill(cod_unbw,18)
        #    cod_unbw = cod_unbw + 1
        
        rows_51_1 = get_rows_51_1(saldo, cons)
        rows_STOCK = get_rows_STOCK(saldo)
        rows_SALDOS = [saldo.row_saldo(),]
        
        wout_1.writerows(rows_51_1)
        wout_2.writerows(rows_STOCK)
        wout_3.writerows(rows_SALDOS)
    

class Command(NoArgsCommand):
    help = "Importar Referencias"
    
    def handle_noargs(self, **options):
        #logging.basicConfig(level=logging.DEBUG, format="%(message)s")
        #logging.info("-" * 72)
        #send_all()
        exp_saldos_sap()
    
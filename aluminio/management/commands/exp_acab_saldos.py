
import logging

from django.core.management.base import NoArgsCommand, BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from settings import ARCH_IMP_ROOT, IMP_REFS

from aluminio.imp_exp import *

ARCH_SALDOS = 'Saldos Formato SAP.txt'


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
        #if saldo.tipo_mat == 'FERT':
        #    s_alum.cod_sap = zfill(cod_fert,18)
        #    cod_fert = cod_fert + 1
        #elif s_alum.tipo_mat == 'UNBW':
        #    s_alum.cod_sap = zfill(cod_unbw,18)
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
    
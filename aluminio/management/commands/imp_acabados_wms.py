
import logging

from django.core.management.base import NoArgsCommand, BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from aluminio.utils import UnicodeReader

from settings import ARCH_IMP_ROOT, IMP_REFS, DELIM_CSV

import csv
import os

from aluminio.models import Acabado, AcabadoSAnt

def get_reader():
    arch = os.path.join(ARCH_IMP_ROOT + os.sep + IMP_REFS['arch_acabados_wms'])
    return UnicodeReader(open(arch, 'rU'),delimiter=DELIM_CSV, encoding='latin1')

class Command(NoArgsCommand):
    help = "Importar acabados WMS"
    
    def handle_noargs(self, **options):
        reader = get_reader()
        i = 0
        for row in reader:
            sw = True
            i = i + 1
            try:
                acab_ant = row[0]
                acab = row[1]
            
                acabado = Acabado.objects.get(nombre=acab)
            except ObjectDoesNotExist:
                sw = False
            except:
                sw = False
            if sw:
                try:
                    acab_wms = AcabadoSAnt.objects.get(sistema='WMS',acab_ant=acab_ant)
                    acab_wms.acabado = acabado
                    acab_wms.save()
                except ObjectDoesNotExist:
                    acab_wms = AcabadoSAnt.objects.create(sistema='WMS',acab_ant=acab_ant,acabado=acabado)
            if not sw:
                print 'Error al importar fila #%i %s' % (i,str(row))
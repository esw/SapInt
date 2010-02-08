
import logging

from django.core.management.base import NoArgsCommand, BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from settings import ARCH_IMP_ROOT, IMP_REFS, DELIM_CSV
from imp_referencias import ref_alum, get_boolean, get_float

import csv
import os

from aluminio.models import Referencia, ReferenciaSAnt

class Command(NoArgsCommand):
    help = "Importar Referencias WMS"
    
    def handle_noargs(self, **options):
        arch = os.path.join(ARCH_IMP_ROOT + os.sep + IMP_REFS['arch_refs_wms'])
        reader = csv.reader(open(arch, 'rU'),delimiter=DELIM_CSV)
        i = 0
        for row in reader:
            sw = True
            i = i + 1
            ref_ant = row[0]
            ref = row[1]
            ale = row[2]
            tem = row[3]
            peso_lineal = get_float(row[4])
            unbw = get_boolean(row[5])
            try:
                referencia = Referencia.objects.get(nombre=ref)
                #referencia = ref_alum(ref,ale,tem,peso_lineal,unbw=unbw)
            except:
                sw = False
            if sw:
                try:
                    ref_wms = ReferenciaSAnt.objects.get(sistema='WMS',ref_ant=ref_ant)
                    ref_wms.referencia = referencia
                    ref_wms.peso_lineal = peso_lineal
                    ref_wms.save()
                except ObjectDoesNotExist:
                    ref_wms = ReferenciaSAnt.objects.create(sistema='WMS',ref_ant=ref_ant,peso_lineal=peso_lineal,referencia=referencia)
            if not sw:
                print 'Error al importar fila #%i %s' % (i,str(row))
            
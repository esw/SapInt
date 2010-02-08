
import logging

from django.core.management.base import NoArgsCommand, BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from settings import ARCH_IMP_ROOT, IMP_REFS, DELIM_CSV

import csv
import os

from aluminio.models import UbicacionSap, UbicacionSAnt

SANT = "WMS"

class Command(NoArgsCommand):
    help = "Importar Referencias"
    
    def handle_noargs(self, **options):
        arch = os.path.join(ARCH_IMP_ROOT + os.sep + IMP_REFS['arch_ubicaciones_wms'])
        reader = csv.reader(open(arch, 'rU'),delimiter=DELIM_CSV)
        i = 0
        for row in reader:
            i = i + 1
            ubi_ant = row[0]
            ubi_sap = row[1]
            area = row[2]
            try:
                ubicacion_sap = UbicacionSap.objects.get(codigo=ubi_sap)
            except ObjectDoesNotExist:
                ubicacion_sap = UbicacionSap.objects.create(codigo=ubi_sap,area=area)
            #if area is not None:
            #    ubicacion_sap.area = area
            #    ubicacion_sap.save()
            if len(UbicacionSAnt.objects.filter(sistema=SANT,ubicacion_ant=ubi_ant)) == 0:
                try:
                    UbicacionSAnt.objects.create(sistema=SANT,ubicacion_ant=ubi_ant,ubicacion_sap=ubicacion_sap)
                except:
                    print 'Error al importar fila #%i %s' % (i,str(row))
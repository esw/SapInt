
import logging

from django.core.management.base import NoArgsCommand, BaseCommand

from settings import ARCH_IMP_ROOT, IMP_REFS, DELIM_CSV

import csv
import os

from aluminio.models import Acabado

class Command(NoArgsCommand):
    help = "Importar Referencias"
    
    def handle_noargs(self, **options):
        #logging.basicConfig(level=logging.DEBUG, format="%(message)s")
        #logging.info("-" * 72)
        #send_all()
        arch = os.path.join(ARCH_IMP_ROOT + os.sep + IMP_REFS['arch_acabados'])
        reader = csv.reader(open(arch, 'rU'),delimiter=DELIM_CSV)
        for row in reader:
            nombre = row[0]
            cod_epics = row[1]
            cod_sap_mat = row[2]
            try:
                acab = Acabado.objects.get(nombre=nombre)
                acab.cod_epics = cod_epics
                acab.cod_sap_mat = cod_sap_mat
                acab.save()
            except:
                pass
                #Acabado(nombre=nombre,cod_epics=cod_epics).save()
    
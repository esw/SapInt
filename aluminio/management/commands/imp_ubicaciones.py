
import logging

from django.core.management.base import NoArgsCommand, BaseCommand

from settings import ARCH_IMP_ROOT, IMP_REFS, DELIM_CSV

import csv
import os

from aluminio.models import UbicacionSap

class Command(NoArgsCommand):
    help = "Importar Referencias"
    
    def handle_noargs(self, **options):
        #logging.basicConfig(level=logging.DEBUG, format="%(message)s")
        #logging.info("-" * 72)
        #send_all()
        arch = os.path.join(ARCH_IMP_ROOT + os.sep + IMP_REFS['arch_ubicaciones'])
        reader = csv.reader(open(arch, 'rU'),delimiter=DELIM_CSV)
        for row in reader:
            codigo = row[0]
            try:
                UbicacionSap.objects.get(codigo=codigo)
            except:
                UbicacionSap(codigo=codigo).save()
    
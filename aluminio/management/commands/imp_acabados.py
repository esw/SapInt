
import logging

from django.core.management.base import NoArgsCommand, BaseCommand

from settings import ARCH_IMP_ROOT, IMP_REFS

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
        reader = csv.reader(open(arch),delimiter=';')
        for row in reader:
            Acabado(nombre=row[0],abreviacion=row[1]).save()
    
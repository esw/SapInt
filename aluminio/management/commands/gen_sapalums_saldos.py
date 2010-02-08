
import logging

from django.core.management.base import NoArgsCommand, BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from settings import ARCH_IMP_ROOT, IMP_REFS

from aluminio.models import *


def gen_sapalums_saldos():
    saldos = SaldoWms.objects.all()
    for saldo in saldos:
        try:
            sapalum = SapAluminio.objects.get(
                referencia = saldo.referencia,
                aleacion = saldo.aleacion,
                temple = saldo.temple,
                acabado = saldo.acabado,
                largo_mm = saldo.largo_mm,
                tipo_mat = saldo.tipo_mat,
                )
            saldo.sapalum = sapalum
            saldo.save()
        except ObjectDoesNotExist:
        #    sapalum = SapAluminio.objects.create(
        #        referencia = saldo.referencia,
        #        aleacion = saldo.aleacion,
        #        temple = saldo.temple,
        #        acabado = saldo.acabado,
        #        largo_mm = saldo.largo_mm,
        #        tipo_mat = saldo.tipo_mat
        #    )
            pass
        

class Command(NoArgsCommand):
    help = "Importar Referencias"
    
    def handle_noargs(self, **options):
        #logging.basicConfig(level=logging.DEBUG, format="%(message)s")
        #logging.info("-" * 72)
        #send_all()
        gen_sapalums_saldos()
    
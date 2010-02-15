
import logging

from django.core.management.base import NoArgsCommand, BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from settings import ARCH_IMP_ROOT, IMP_REFS, DELIM_CSV

import csv
import os

from aluminio.models import Referencia,Acabado,Aleacion,Temple,SapAluminio

COL_REFS = {
    'referencia':0,
    'pesolineal':1,
    'perim_exp':2,
}

def get_reader():
    arch = os.path.join(ARCH_IMP_ROOT + os.sep + IMP_REFS['arch_refs_pexp'])
    return csv.reader(open(arch, 'rU'),delimiter=DELIM_CSV)

BOOL_TRUE_VALS = ['TRUE','True','1','Verdadero','VERDADERO','V','v','SI','si','Si','T','t','U']

def get_boolean(string):
    if string in BOOL_TRUE_VALS: return True
    return False

def get_float(string):
    if string is not None and string != '':
        return float(string.replace(',','.'))
    else: return None

def get_aleacion(codigo):
    return Aleacion.objects.get(codigo=codigo)

def get_temple(codigo):
    return Temple.objects.get(codigo=codigo)

def get_ref(nombre,peso_lineal,perim_exp):
    ref = Referencia.objects.get(nombre=nombre)
    if ref:
        ref.peso_lineal = peso_lineal
        ref.perim_exp = perim_exp
        ref.save()
    return ref

def ref_alum(referencia,peso_lineal,perim_exp):
    peso_lineal = get_float(peso_lineal)
    perim_exp = get_float(perim_exp)
    ref = get_ref(referencia,peso_lineal,perim_exp)
    return ref

class Command(NoArgsCommand):
    help = "Importar Referencias"
    
    def handle_noargs(self, **options):
        #logging.basicConfig(level=logging.DEBUG, format="%(message)s")
        #logging.info("-" * 72)
        #send_all()
        reader = get_reader()
        i = 0
        for row in reader:
            i = i + 1
            try:
                al = ref_alum(
                    referencia = row[COL_REFS['referencia']],
                    peso_lineal = row[COL_REFS['pesolineal']],
                    perim_exp = row[COL_REFS['perim_exp']],
                )
            except:
                print 'Error al importar fila #%i %s' % (i,str(row))
    
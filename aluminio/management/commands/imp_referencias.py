
import logging

from django.core.management.base import NoArgsCommand, BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from settings import ARCH_IMP_ROOT, IMP_REFS, DELIM_CSV

import csv
import os

from aluminio.models import Referencia,Acabado,Aleacion,Temple,SapAluminio

COL_REFS = {
    'referencia':0,
    'aleacion':1,
    'temple':2,
    'pesolineal':3,
    #'perim_exp':4,
    'unbw':4,
}

def get_reader():
    arch = os.path.join(ARCH_IMP_ROOT + os.sep + IMP_REFS['arch_refs'])
    return csv.reader(open(arch, 'rU'),delimiter=DELIM_CSV)

BOOL_TRUE_VALS = ['TRUE','True','1','Verdadero','VERDADERO','SI','si','Si','T','t','U']

def get_boolean(string):
    if string in BOOL_TRUE_VALS: return True
    return False

def get_float(string):
    if string is not None and string != '':
        return float(string.replace(',','.'))
    else: return None

def get_aleacion(codigo):
    try:
        return Aleacion.objects.get(codigo=codigo)
    except:
        return Aleacion.objects.create(codigo=codigo)

def get_temple(codigo):
    try:
        return Temple.objects.get(codigo=codigo)
    except:
        return Temple.objects.create(codigo=codigo)

def get_ref(nombre,peso_lineal,aleacion,temple,perim_exp=None,perim_total=None,unbw=False):
    try:
        ref = Referencia.objects.get(nombre=nombre)
        if ref:
            ref.aleacion_std = aleacion
            ref.temple_std = temple
            ref.peso_lineal = peso_lineal
            ref.perim_exp = perim_exp
            ref.perim_total = perim_total
            ref.unbw = unbw
            ref.save()
        return ref
    except ObjectDoesNotExist:
        return Referencia.objects.create(
            nombre = nombre,
            peso_lineal = peso_lineal,
            aleacion_std = aleacion,
            temple_std = temple,
            perim_exp = perim_exp,
            perim_total = perim_total,
            unbw = unbw
        )

def ref_alum(referencia,aleacion,temple,peso_lineal,perim_exp=None,unbw=False,perim_total=None):
    ale = get_aleacion(aleacion)
    tem = get_temple(temple)
    peso_lineal = get_float(peso_lineal)
    perim_exp = get_float(perim_exp)
    perim_total = get_float(perim_total)
    ref = get_ref(referencia,peso_lineal,ale,tem,perim_exp,perim_total,unbw)
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
                    aleacion = row[COL_REFS['aleacion']],
                    temple = row[COL_REFS['temple']],
                    peso_lineal = row[COL_REFS['pesolineal']],
                    #perim_exp = row[COL_REFS['perim_exp']],
                    perim_exp = None,
                    unbw = get_boolean(row[COL_REFS['unbw']]),
                )
            except:
                print 'Error al importar fila #%i %s' % (i,str(row))
    
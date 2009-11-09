
import logging

from django.core.management.base import NoArgsCommand, BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from settings import ARCH_IMP_ROOT, IMP_REFS

import csv
import os

from aluminio.models import Referencia,Acabado,Aleacion,Temple,RefLegacy,SapAluminio

COL_REFS = {
    'referencia':0,
    'acabado':1,
    'aleacion':2,
    'temple':3,
    'long_mm':4,
    'pesolineal':5,
    'tipo_mat':6,
}

class Command(NoArgsCommand):
    help = "Importar Referencias"
    
    def get_acabado(self,nombre):
        try:
            return Acabado.objects.get(nombre=nombre)
        except:
            return Acabado.objects.create(nombre=nombre)
    
    def get_aleacion(self,codigo):
        try:
            return Aleacion.objects.get(codigo=codigo)
        except:
            return Aleacion.objects.create(codigo=codigo)
    
    def get_temple(self,codigo):
        try:
            return Temple.objects.get(codigo=codigo)
        except:
            return Temple.objects.create(codigo=codigo)
    
    def get_ref(self,nombre,peso_lineal,aleacion,temple,perim_exp=None,perim_total=None):
        try:
            return Referencia.objects.get(nombre=nombre)
        except:
            return Referencia.objects.create(
                nombre=nombre,
                peso_lineal=float(peso_lineal.replace(',','.')),
                aleacion_std=aleacion,
                temple_std=temple,
                perim_exp=perim_exp,
                perim_total=perim_total
            )
    
    def sap_alum(self,referencia,acabado,aleacion,temple,largo_mm,peso_lineal,tipo_mat=None,perim_exp=None,perim_total=None):
        acab = self.get_acabado(acabado)
        ale = self.get_aleacion(aleacion)
        tem = self.get_temple(temple)
        ref = self.get_ref(referencia,peso_lineal,ale,tem,perim_exp,perim_total)
        try:
            sapalum = SapAluminio.objects.get(referencia=ref,acabado=acab,temple=tem,aleacion=ale,largo_mm=largo_mm,tipo_mat=tipo_mat)
        except ObjectDoesNotExist:
            sapalum = SapAluminio.objects.create(referencia=ref,acabado=acab,temple=tem,aleacion=ale,largo_mm=largo_mm,tipo_mat=tipo_mat)
        return sapalum
    
    def handle_noargs(self, **options):
        #logging.basicConfig(level=logging.DEBUG, format="%(message)s")
        #logging.info("-" * 72)
        #send_all()
        arch = os.path.join(ARCH_IMP_ROOT + os.sep + IMP_REFS['arch_refs'])
        reader = csv.reader(open(arch),delimiter=';')
        for row in reader:
            al = self.sap_alum(
                referencia = row[COL_REFS['referencia']],
                acabado = row[COL_REFS['acabado']],
                aleacion = row[COL_REFS['aleacion']],
                temple = row[COL_REFS['temple']],
                largo_mm = row[COL_REFS['long_mm']],
                peso_lineal = row[COL_REFS['pesolineal']],
                tipo_mat = row[COL_REFS['tipo_mat']]
            )
            print al
    
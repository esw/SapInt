
import logging

from django.core.management.base import NoArgsCommand, BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from settings import ARCH_IMP_ROOT, IMP_REFS, DELIM_CSV

import csv
import os

from aluminio.models import Referencia,Acabado,Aleacion,Temple,SapAluminio

COL_REFS = {
    'referencia':0,
    'acabado':1,
    'aleacion':2,
    'temple':3,
    'largo_mm':4
}

class Command(NoArgsCommand):
    help = "Importar Referencias"
    
    def get_acabado(self,nombre):
        return Acabado.objects.get(nombre=nombre)
    
    def get_aleacion(self,ref,codigo):
        try:
            return Aleacion.objects.get(codigo=codigo)
        except:
            return ref.aleacion_std
    
    def get_temple(self,ref,codigo):
        try:
            return Temple.objects.get(codigo=codigo)
        except:
            return ref.temple_std
    
    def get_ref(self,nombre):
        return Referencia.objects.get(nombre=nombre)
    
    def sap_alum(self,referencia,acabado,aleacion,temple,largo_mm):
        sapalum, sapalum2 = None, None
        ref = self.get_ref(referencia)
        acab = self.get_acabado(acabado)
        ale = self.get_aleacion(ref, aleacion)
        tem = self.get_temple(ref, temple)
        unbw = ref.unbw
        try:
            sapalum = SapAluminio.objects.get(referencia=ref,acabado=acab,temple=tem,aleacion=ale,largo_mm=largo_mm,tipo_mat='FERT')
        except ObjectDoesNotExist:
            sapalum = SapAluminio.objects.create(referencia=ref,acabado=acab,temple=tem,aleacion=ale,largo_mm=largo_mm) 
        if unbw:
            try:
                sapalum2 = SapAluminio.objects.get(referencia=ref,acabado=acab,temple=tem,aleacion=ale,largo_mm=largo_mm,tipo_mat='UNBW')
            except:
                sapalum2 = SapAluminio.objects.create(referencia=ref,acabado=acab,temple=tem,aleacion=ale,largo_mm=largo_mm,tipo_mat='UNBW')
        return sapalum, sapalum2
    
    def handle_noargs(self, **options):
        arch = os.path.join(ARCH_IMP_ROOT + os.sep + IMP_REFS['arch_alums'])
        reader = csv.reader(open(arch,'rU'),delimiter=DELIM_CSV)
        i = 0
        for row in reader:
            i = i + 1
            try:
                al, al2 = self.sap_alum(
                    referencia = row[COL_REFS['referencia']],
                    acabado = row[COL_REFS['acabado']],
                    aleacion = row[COL_REFS['aleacion']],
                    temple = row[COL_REFS['temple']],
                    largo_mm = row[COL_REFS['largo_mm']]
                )
                #print al
                #if al2: print al2
            except:
                print 'Error al importar fila #%i %s' % (i,str(row))
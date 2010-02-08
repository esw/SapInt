
import logging

from django.core.management.base import NoArgsCommand, BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from settings import ARCH_IMP_ROOT, IMP_REFS, DELIM_CSV
from aluminio.imp_exp import get_writer

import csv
import os

from aluminio.models import Referencia,Acabado,Aleacion,Temple,SapAluminio, check_tipo_by_cod

COL_REFS = {
    'cod_sap':0,
    'referencia':1,
    'acabado':2,
    'aleacion':3,
    'temple':4,
    'long_mm':5,
}

WRITER = None

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
    
    def get_ref(self,nombre,aleacion,temple,peso_lineal=None,perim_exp=None,perim_total=None):
        try:
            return Referencia.objects.get(nombre=nombre)
        except:
            if peso_lineal is None: return None
            if perim_exp is not None: perim_exp = float(perim_exp.replace(',','.'))
            if perim_total is not None: perim_total = float(perim_total.replace(',','.'))
            return Referencia.objects.create(
                nombre = nombre,
                peso_lineal = float(peso_lineal.replace(',','.')),
                aleacion_std = aleacion,
                temple_std = temple,
                perim_exp = perim_exp,
                perim_total = perim_total,
            )
    
    def sap_alum(self,cod_sap,referencia,acabado,aleacion,temple,largo_mm,peso_lineal=None,tipo_mat=None,perim_exp=None,perim_total=None):
        acab = self.get_acabado(acabado)
        ale = self.get_aleacion(aleacion)
        tem = self.get_temple(temple)
        ref = self.get_ref(referencia,ale,tem,peso_lineal,perim_exp,perim_total)
        #if cod_sap is None or cod_sap == '': t_mat = 'FERT'
        if tipo_mat is None: t_mat = check_tipo_by_cod(cod_sap)
        else: t_mat = tipo_mat
        try:
            sapalum = SapAluminio.objects.get(referencia=ref,acabado=acab,temple=tem,aleacion=ale,largo_mm=largo_mm,tipo_mat=t_mat)
            #WRITER.writerow(sapalum.row_lista())
            #print 'Repetido:' + str(sapalum.row_lista())
            #if sapalum.cargado is False:
            sapalum.cargado = True
            sapalum.cod_sap = cod_sap
            sapalum.save()
            #WRITER.writerow((sapalum.row_lista())
        except ObjectDoesNotExist:
            sapalum = SapAluminio.objects.create(cod_sap=cod_sap,referencia=ref,acabado=acab,temple=tem,aleacion=ale,largo_mm=largo_mm,tipo_mat=t_mat,cargado=True)
        
        return sapalum
    
    def handle_noargs(self, **options):
        #logging.basicConfig(level=logging.DEBUG, format="%(message)s")
        #logging.info("-" * 72)
        #send_all()
        arch = os.path.join(ARCH_IMP_ROOT + os.sep + IMP_REFS['arch_sapalums'])
        reader = csv.reader(open(arch, 'rU'),delimiter=DELIM_CSV)
        #WRITER = get_writer('REPETIDOS.txt')
        i = 0
        for row in reader:
            i = i + 1
            try:
                al = self.sap_alum(
                    cod_sap = row[COL_REFS['cod_sap']],
                    referencia = row[COL_REFS['referencia']],
                    acabado = row[COL_REFS['acabado']],
                    aleacion = row[COL_REFS['aleacion']],
                    temple = row[COL_REFS['temple']],
                    largo_mm = row[COL_REFS['long_mm']]
                )
            except:
                print 'Error al importar fila #%i %s' % (i,str(row)) 
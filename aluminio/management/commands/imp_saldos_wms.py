
import logging

from django.core.management.base import NoArgsCommand, BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from settings import ARCH_IMP_ROOT, IMP_REFS, DELIM_CSV
from imp_referencias import get_boolean, get_float

from aluminio.utils import UnicodeReader

import csv
import os

from aluminio.models import *

def get_ref(ref):
    ref_wms = ReferenciaSAnt.objects.get(sistema='WMS',ref_ant=ref)
    return ref_wms.referencia    

SANT = 'WMS'

class Command(NoArgsCommand):
    help = "Importar Saldos WMS"
    
    def handle_noargs(self, **options):
        arch = os.path.join(ARCH_IMP_ROOT + os.sep + IMP_REFS['arch_saldos_wms'])
        reader = UnicodeReader(open(arch, 'rU'),delimiter=DELIM_CSV, encoding='latin1')
        i = 0
        for row in reader:
            i = i + 1
            sw = True
            cod = row[0]
            res = row[1]
            ubi = row[2]
            ref = row[3]
            acab = row[4]
            largo = int(row[5])
            proy = row[6]
            cant = int(row[7])
            grpv = row[8]
            #precio = row[9]
            precio = None
            tmat = row[10]
            
            try:
                referencia = ReferenciaSAnt.objects.get(sistema=SANT,ref_ant=ref).referencia
                aleacion = referencia.aleacion_std
                temple = referencia.temple_std
                ubicacion = UbicacionSAnt.objects.get(sistema=SANT,ubicacion_ant=ubi).ubicacion_sap
                acabado = AcabadoSAnt.objects.get(sistema=SANT,acab_ant=acab).acabado
                grupo_val = None
                try:
                    if grpv is None or grpv =='': grupo_val = acabado.grupo_val
                    else: grupo_val = GrupoValoracion.objects.get(codigo=grpv)
                except ObjectDoesNotExist:
                    grupo_val = None
            except ReferenciaSAnt.DoesNotExist:
                sw = False
                print 'Referencia Anterior %s no Existe' % ref
            except UbicacionSAnt.DoesNotExist:
                sw = False
                print 'Ubicacion Anterior %s no Existe' % ubi
            except AcabadoSAnt.DoesNotExist:
                sw = False
                print 'Acabado Anterior %s no Existe' % acab
            except ObjectDoesNotExist:
                sw = False
            
            if precio is not None and precio !='': precio = int(precio)
            else: precio = None
            
            if sw:
                if res =='': res = None
                SaldoWms.objects.create(
                    codigo = cod,
                    reserva = res,
                    referencia = referencia,
                    aleacion = aleacion,
                    temple = temple,
                    acabado = acabado,
                    largo_mm = largo,
                    ubicacion = ubicacion,
                    cant = cant,
                    proyecto = proy,
                    tipo_mat = tmat,
                    precio = precio,
                    grupo_val = grupo_val
                    )
            if not sw:
                print 'Error al importar fila #%i %s' % (i,str(row))            
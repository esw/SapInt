import csv
import os
from settings import ARCH_EXP_DIR, ARCH_EXP_ROOT
from aluminio.models import *

ARCH_32_1 = '32_1_Material_Datos_Basicos.txt'
ARCH_32_2 = '32_2_Material_Plant_GEN.txt'
ARCH_BOM_PP = 'BOM_PP.txt'

DELIM = '\t'
LTERM = '\n'

ROW_HEADS_32_1 = [
    'SAP_MAT_NUM',      #1  Codigo SAP
    'OLD_MAT_NUM',      #2  Codigo Antiguo
    'MAT_TYPE',         #3  Tipo Material
    'INDT_SECT',        #4  Sector Industria
    'DESC',             #5  Descripcion
    'BASE_UOM',         #6  Unidad Base
    'MATL_GRP',         #7  Grupo Articulos
    'WGT_UOM',          #15 Unidad Peso
    'CONFIG_MAT_IND',   #21 Indicador Material Configurable
    'TRP_GRP',          #24 Grupo Transporte    
]

VTIPOS = {
    'Texto':'T',
    'Campo':'C',
    'Funcion':'F',
    'Parametro':'P',
}

DICT_ROW_32_1 = [
    { 'header':'SAP_MAT_NUM', 'tipo':'C', 'valor':'cod_sap', 'desc':'Codigo SAP' },
    { 'header':'OLD_MAT_NUM', 'tipo':'C', 'valor':'cod_sap' },
    { 'header':'MAT_TYPE', 'tipo':'C', 'valor':'tipo_mat' },
    { 'header':'INDT_SECT', 'tipo':'T', 'valor':'M' },
    { 'header':'DESC', 'tipo':'C', 'valor':'desc' },
    { 'header':'BASE_UOM', 'tipo':'T', 'valor':'KG' },
    { 'header':'MATL_GRP', 'tipo':'T', 'valor':'YBR02' },
    { 'header':'WGT_UOM', 'tipo':'T', 'valor':'KG' },
    { 'header':'CONFIG_MAT_IND', 'tipo':'T', 'valor':'X' },
    { 'header':'TRP_GRP', 'tipo':'T', 'valor':'0001' },
]

def get_rows_32_1_m(sap_alum):
    row = [
        sap_alum.cod_sap,   #1  Codigo SAP
        sap_alum.cod_sap,   #2  Codigo Antiguo
        sap_alum.tipo_mat,  #3  Tipo Material
        'M',                #4  Sector Industria
        sap_alum.desc,      #5  Descripcion
        'KG',               #6  Unidad Base
        'YBR02',            #7  Grupo Articulos
        'KG',               #15 Unidad de Peso
        'X',                #21 Material Configurable
        '0001',             #24 Grupo Transporte
    ]
    rows = [row,]
    return rows

def get_value_from_dict(d,sap_alum,**kwargs):
    if d['tipo'] == 'C':
        return getattr(sap_alum,d['valor'])
    if d['tipo'] == 'T':
        return d['valor']
    if d['tipo'] == 'P':
        return kwargs[d['valor']]

def get_row_from_dicts(dicts,obj,**kwargs):
    row = []
    for d in dicts:
        row.append(get_value_from_dict(d,obj,**kwargs))
    return row
    
def get_rows_32_1(sap_alum):
    return [get_row_from_dicts(DICT_ROW_32_1,sap_alum),]

def get_rows_32_1_all(sap_alum):
    row = [
        sap_alum.cod_sap,   #1  Codigo SAP
        sap_alum.cod_sap,   #2  Codigo Antiguo
        sap_alum.tipo_mat,  #3  Tipo Material
        sap_alum.desc,      #4  Descripcion
        'M',                #5  Sector Industria
        'KG',               #6  Unidad Base
        'YBR02',            #7  Grupo Articulos
        '',                 #8  Grupo Articulos Externo
        '',                 #9  Lab/Oficina de Proyectos
        '',                 #10 Sector
        '',                 #11 Jerarquia Producto
        '',                 #12 Status material Centros
        '',                 #13 Fecha Inicio Status
        '',                 #14 Grupo Tipos Posicion General
        'KG',               #15 Unidad de Peso
        '',                 #16 Peso Bruto
        '',                 #17 Peso Neto
        '',                 #18 Unidad Volumen
        '',                 #19 Volumen
        '',                 #20 Tamano/Dimension
        'X',                #21 Material Configurable
        '',                 #22 Indicador Sujeto a Lote
        '',                 #23 Clave Valores de Compra
        '0001',             #24 Grupo Transporte
        '',                 #25 Nivel Univocidad
        '',                 #26 Condiciones Almacenaje
        '',                 #27 Duracion Minima
        '',                 #28 Duracion Total
        '',                 #29 Porcentaje Alm
        '',                 #30 Indicador Periodo de Caducidad
        '',                 #31 Indicador Mat Peligroso
        '',                 #32 Relevante MedioAmbiente
        '',                 #33 Grupo Mat Embalaje
        '',                 #34 Tipo Mat Embalaje
        '',                 #35 Tipo Numero Articulo Eu
        '',                 #36 Num Articulo Eu (EAN)
    ]
    rows = [row,]
    return rows

ROW_HEADS_32_2 = [
    'MAT_NUM',      #1  Codigo SAP
    'OLD_MAT_REF',  #2  Codigo Antiguo
    'PLANT',        #3  Centro
    'AVAIL_CHK',    #45 Grupo Verif de Disponibilidad
    'VAL_CLASS',    #62 Categoria Valoracion
    'PRCTR',        #72 Centro Beneficio
]

DICT_ROW_32_2 = [
    { 'header':'SAP_MAT_NUM', 'tipo':'C', 'valor':'cod_sap', 'desc':'Codigo SAP' },
    { 'header':'OLD_MAT_NUM', 'tipo':'C', 'valor':'cod_sap' },
    { 'header':'PLANT', 'tipo':'P', 'valor':'centro' },
    { 'header':'AVAIL_CHK', 'tipo':'T', 'valor':'Y2' },
    { 'header':'VAL_CLASS', 'tipo':'T', 'valor':'E103' },
    { 'header':'PRCTR', 'tipo':'P', 'valor':'centro_benef' },
]

def get_row_32_2(sap_alum,centro,centro_benef):
    return get_row_from_dicts(DICT_ROW_32_2,sap_alum,centro=centro,centro_benef=centro_benef)

def get_row_32_2_o(sap_alum,centro,centro_benef):
    row = [
        sap_alum.cod_sap,   #1  Codigo SAP
        sap_alum.cod_sap,   #2  Codigo Antiguo
        centro,             #3  Centro
        'Y2',               #45 Grupo Verif de Disponibilidad
        'E103',             #62 Categoria Valoracion
        centro_benef,       #72 Centro Beneficio
    ]
    return row

def get_row_32_2_all(sap_alum,centro,centro_benef):
    row = [
        sap_alum.cod_sap,   #1  Codigo SAP
        sap_alum.cod_sap,   #2  Codigo Antiguo
        centro,             #3  Centro
        '',                 #4  Grupo Carga
        '',                 #5  Perfil Num Serie
        '',                 #6  GrupoMat ComExt
        '',                 #7  No EstadMerc/CodImportacion
        '',                 #8  Pais OrigenMat
        '',                 #9  Ind Pedido Automat Perm
        '',                 #10 Tiempo trat Entrada Merc
        '',                 #11 Indic Sujeto Pedido
        '',                 #12 Grupo Plan Nec
        '',                 #13 Grupo Compras
        '',                 #14 Indic ABC
        '',                 #15 Status Mat x Centro
        '',                 #16 Fecha Val Status MAT/MPPS
        '',                 #17 Carac Plan Nec
        '',                 #18 Punto Pedido
        '',                 #19 Planif Nececidades
        '',                 #20 Tamano Lote Planif
        '',                 #21 Tamano Lote Min
        '',                 #22 Tamano Lote Max
        '',                 #23 Tamano Lote Fijo
        '',                 #24 Stock Maximo
        '',                 #25 Rechazo
        '',                 #26 Valor Redondeo Cant Pedir
        '',                 #27 Cadencia
        '',                 #28 Clase Aprovicionamiento
        '',                 #29 Clase Aprovicionamiento Especial
        '',                 #30 Almacen Produccion
        '',                 #31 Almacen Propuesto para Aprov Ext
        '',                 #32 Indicador Toma Retroactiva
        '',                 #33 Indicador Mat Granel
        '',                 #34 Tiempo Fabricacion Propia
        '',                 #35 Plazo Entrega Previsto
        '',                 #36 Clave Horizonte
        '',                 #37 Stock Seguridad
        '',                 #38 Nivel Servicio
        '',                 #39 Indicador Margen de Seguridad
        '',                 #40 Tipo Margen Seguridad
        '',                 #41 Grupo Estrategia Planif
        '',                 #42 Modo Compensacion
        '',                 #43 Intervalo Compensacion hacia Atras
        '',                 #44 Intervalo Compensacion hacia Adelante
        'Y2',               #45 Grupo Verif de Disponibilidad
        '',                 #46 Tiempo Total Reposicion
        '',                 #47 Indic Seleccion Lista Mat Alternativas
        '',                 #48 Indic Permite Fabric Repetitiva
        '',                 #49 Perfil de Fabric Repetitiva
        '',                 #50 Rechazo Nivel Componente %
        '',                 #51 Indic Nec Secundarias
        '',                 #52 Indic Agrupamiento Necesidades
        '',                 #53 Reponsable Control Produccion
        '',                 #54 Limite Tolerancia Entrega incompleta
        '',                 #55 Limite Tolerancia Exceso Suministro
        '',                 #56 Tiempo Preparacion
        '',                 #57 Tiempo Transito
        '',                 #58 Tiempo Tratamiento
        '',                 #59 Cantidad Base
        '',                 #60 Indic Inv para Recuento Ciclico
        '',                 #61 Tiempo Almac Maximo
        'E103',             #62 Categoria Valoracion
        '',                 #63 Indic Control Precios
        '',                 #64 Cantidad Base
        '',                 #65 Precio Estandard
        '',                 #66 Precio Medio Variable
        '',                 #67 No Efectuar CC
        '',                 #68 Se calcula con Estruc Cuantit
        '',                 #69 Origen con Referencia a Mat
        '',                 #70 Clave Desviacion
        '',                 #71 Tamano Lote para calculo de costo
        centro_benef,       #72 Centro Beneficio
        '',                 #73 Precio Previsto 1
        '',                 #74 Fecha Precio Plan 1
        '',                 #75 Perfil Control Fabricacion
        '',                 #76 Indic Planif Nece Mixta
        '',                 #77 Grupo Origenes
    ]
    return row

def get_rows_32_2(sap_alum):
    rows = []
    rows.append(get_row_32_2(sap_alum,centro='1100',centro_benef=''))
    rows.append(get_row_32_2(sap_alum,centro='1110',centro_benef=''))
    if sap_alum.tipo_mat != 'HALB':
        rows.append(get_row_32_2(sap_alum,centro='1010',centro_benef=''))
    return rows

def get_writer(nombre):
    return csv.writer(
        open(os.path.abspath(ARCH_EXP_ROOT + os.sep + nombre),'w'),
        delimiter = DELIM,
        lineterminator = LTERM
    )

DICT_ROW_BOM_PP = [
    { 'header':'MATNR', 'tipo':'C', 'valor':'cod_sap', 'desc':'Codigo SAP' },
    { 'header':'WERKS', 'tipo':'P', 'valor':'centro', 'desc':'Codigo Centro' },
    { 'header':'STLAN', 'tipo':'T', 'valor':'', 'desc':'Utilizacion' },
    { 'header':'STLAL', 'tipo':'T', 'valor':'1', 'desc':'Alternativa de la Lista' },
    { 'header':'DATUV', 'tipo':'T', 'valor':'', 'desc':'Validez' },
    { 'header':'BMENG', 'tipo':'C', 'valor':'peso_kg', 'desc':'Cantidad Base' },
    { 'header':'BMEIN', 'tipo':'T', 'valor':'KG', 'desc':'Unidad Base' },
    { 'header':'ZTEXT', 'tipo':'C', 'valor':'desc', 'desc':'Texto de la Lista de Mat' },
    { 'header':'STKTX', 'tipo':'T', 'valor':'', 'desc':'Texto de la alternativa de Lista Mat' },
    { 'header':'POSNR', 'tipo':'P', 'valor':'num_pos', 'desc':'# de Posicion de Lista Mat' },
    { 'header':'POSTP', 'tipo':'T', 'valor':'L', 'desc':'Tipo de Posicion' },
    { 'header':'IDNRK', 'tipo':'P', 'valor':'cod_comp', 'desc':'Codigo de Componente' },
    { 'header':'KTEXT', 'tipo':'T', 'valor':'', 'desc':'Descripcion del Componente' },
    { 'header':'MENGE', 'tipo':'P', 'valor':'cant_comp', 'desc':'Cantidad de Componente' },
    { 'header':'MEINS', 'tipo':'P', 'valor':'uni_comp', 'desc':'UnidadMedida Componente' },
    { 'header':'FMENG', 'tipo':'T', 'valor':'', 'desc':'Cantidad Fija' },
    { 'header':'AUSCH', 'tipo':'P', 'valor':'rech_comp', 'desc':'Rechazo Componente %' },
    { 'header':'KZKUP', 'tipo':'T', 'valor':'', 'desc':'Indicador Co-Producto' },
    { 'header':'REKRS', 'tipo':'T', 'valor':'', 'desc':'Indicador Recursividad Permitida' },
    { 'header':'DSPST', 'tipo':'T', 'valor':'', 'desc':'Control Explosion' },
    { 'header':'RC29P-SANKA', 'tipo':'T', 'valor':'X', 'desc':'Relevancia de Costos' },
    { 'header':'RC29P-LGORT', 'tipo':'P', 'valor':'almacen', 'desc':'Almacen' },
    { 'header':'KNSRT', 'tipo':'T', 'valor':'', 'desc':'Clasificacion' },
    { 'header':'KNNAM', 'tipo':'T', 'valor':'', 'desc':'Relacion' },
    { 'header':'DOKNR', 'tipo':'T', 'valor':'', 'desc':'Documento' },
    { 'header':'DOKAR', 'tipo':'T', 'valor':'', 'desc':'Clase de Documento' },
    { 'header':'DOKTL_D', 'tipo':'T', 'valor':'', 'desc':'Doc Parcial' },
    { 'header':'DOKVR', 'tipo':'T', 'valor':'', 'desc':'Version' },
    #{ 'header':'', 'tipo':'', 'valor':'', 'desc':'' },
]

def get_row_bom_pp(sap_alum,centro,num_pos,cod_comp,cant_comp,uni_comp,rech_comp,almacen):
    
    # Genero Row Aluminio
    return get_row_from_dicts(
        DICT_ROW_BOM_PP,
        sap_alum,
        centro=centro,
        num_pos=num_pos,
        cod_comp=cod_comp,
        cant_comp=cant_comp,
        uni_comp=uni_comp,
        rech_comp=rech_comp,
        almacen=almacen,
        )

def get_rows_bom_pp(sap_alum):
    rows = []
    cod_comp = ALUM_COD_SAP_MAT
    cant_comp = sap_alum.peso_kg + (sap_alum.peso_kg * 0.20)
    rows.append(get_row_bom_pp(sap_alum,centro='1010',num_pos='0010',cod_comp=cod_comp,cant_comp=cant_comp,uni_comp='KG',rech_comp='',almacen='1050'))
    cod_comp = SCRAP_COD_SAP_MAT
    cant_comp = sap_alum.peso_kg * -0.20
    rows.append(get_row_bom_pp(sap_alum,centro='1010',num_pos='0010',cod_comp=cod_comp,cant_comp=cant_comp,uni_comp='KG',rech_comp='',almacen='1050'))
    cod_comp = sap_alum.cod_acabado
    cant_comp = sap_alum.cant_acabado
    if sap_alum.pintado: rows.append(get_row_bom_pp(sap_alum,centro='1010',num_pos='0020',cod_comp=cod_comp,cant_comp=cant_comp,uni_comp='GAL',rech_comp='',almacen='1050'))
    cod_comp = sap_alum.cod_primer
    cant_comp = sap_alum.cant_primer
    if sap_alum.primer: rows.append(get_row_bom_pp(sap_alum,centro='1010',num_pos='0030',cod_comp=cod_comp,cant_comp=cant_comp,uni_comp='GAL',rech_comp='',almacen='1050'))
    return rows

def exp_alum_mat():
    wout_1 = get_writer(ARCH_32_1)
    wout_2 = get_writer(ARCH_32_2)
    wout_3 = get_writer(ARCH_BOM_PP)
    wout_1.writerow(ROW_HEADS_32_1)
    wout_2.writerow(ROW_HEADS_32_2)
    for s_alum in SapAluminio.objects.all():
        rows_32_1 = get_rows_32_1(s_alum)
        rows_32_2 = get_rows_32_2(s_alum)
        rows_bom_pp = get_rows_bom_pp(s_alum)
        wout_1.writerows(rows_32_1)
        wout_2.writerows(rows_32_2)
        wout_3.writerows(rows_bom_pp)
    
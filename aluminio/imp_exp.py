import csv
import os
from settings import ARCH_EXP_DIR, ARCH_EXP_ROOT
from aluminio.models import *
from datetime import date

ARCH_32_1 = '32_1_Material_Datos_Basicos.txt'
ARCH_32_2 = '32_2_Material_Plant_GEN.txt'
ARCH_32_3 = '32_3.txt'
ARCH_32_4 = '32_4.txt'
ARCH_32_5 = '32_5.txt'
ARCH_32_6 = '32_6.txt'
ARCH_32_A = '32_A.txt'
ARCH_CDATA = 'Cambios Data Maestra.txt'
ARCH_LISTA = 'Listado Materiales SAP.txt'
ARCH_VFAB = 'PP Versiones de Fabricacion.txt'
ARCH_BOM_PP = 'PP Listas de Material.txt'

DELIM = '\t'
LTERM = '\n'

def get_writer(nombre):
    return csv.writer(
        open(os.path.abspath(ARCH_EXP_ROOT + os.sep + nombre),'w'),
        delimiter = DELIM,
        lineterminator = LTERM
    )

VTIPOS = {
    'Texto':'T',
    'Campo':'C',
    'Funcion':'F',
    'Parametro':'P',
}

def fecha_dia():
    t = date.today()
    return '%s%s%s' % (zfill(t.day,2),zfill(t.month,2),t.year)

def get_value_from_dict(d,sap_alum,**kwargs):
    if d['tipo'] == 'C':
        return str(getattr(sap_alum,d['valor']))
    if d['tipo'] == 'T':
        return d['valor']
    if d['tipo'] == 'P':
        return kwargs[d['valor']]

def get_headers_from_dicts(dicts):
    headers = []
    for d in dicts:
        headers.append(d['header'])
    return headers

def eval_add_tipo(d,sap_alum,**kwargs):
    if sap_alum.tipo_mat in d:
        return d[sap_alum.tipo_mat]
    return True
    
def get_row_from_dicts(dicts,obj,**kwargs):
    row = []
    for d in dicts:
        if eval_add_tipo(d,obj,**kwargs):
            row.append(get_value_from_dict(d,obj,**kwargs))
        else: row.append('')
    return row


DICT_ROW_32_1 = [
    { 'header':'SAP_MAT_NUM', 'tipo':'C', 'valor':'cod_sap', 'desc':'Codigo SAP' },
    { 'header':'MAT_TYPE', 'tipo':'C', 'valor':'tipo_mat' },
    { 'header':'INDT_SECT', 'tipo':'T', 'valor':'M' },
    { 'header':'DESC', 'tipo':'C', 'valor':'desc' },
    { 'header':'BASE_UOM', 'tipo':'T', 'valor':'KG' },
    { 'header':'MATL_GRP', 'tipo':'T', 'valor':'ZPT04' },
    { 'header':'DIVISION', 'tipo':'T', 'valor':'10' },
    { 'header':'GEN_ITEM_CAT_GRP', 'tipo':'T', 'valor':'NORM' },
    { 'header':'WGT_UOM', 'tipo':'T', 'valor':'KG' },
    { 'header':'WGT_GRS', 'tipo':'T', 'valor':'01' },
    { 'header':'WGT_NET', 'tipo':'T', 'valor':'01' },
    { 'header':'PURCH_VAL_KEY', 'tipo':'T', 'valor':'Z02' },
    { 'header':'TRP_GRP', 'tipo':'T', 'valor':'0001' },
    { 'header':'STO_COND', 'tipo':'T', 'valor':'01' },
]
    
def get_rows_32_1(sap_alum):
    return [get_row_from_dicts(DICT_ROW_32_1,sap_alum),]


DICT_ROW_32_2_ES = [
    { 'header':'MAT_NUM', 'tipo':'C', 'valor':'cod_sap', 'desc':'Codigo SAP' },
    { 'header':'PLANT', 'tipo':'T', 'valor':'1100' },
    { 'header':'LOAD_GRP', 'tipo':'T', 'valor':'0001', 'UNBW':False },
    { 'header':'UMA_UMP', 'tipo':'T', 'valor':'UN' },
    { 'header':'UMA_UMPA', 'tipo':'T', 'valor':'2' },
    { 'header':'MRP_TYPE', 'tipo':'T', 'valor':'ND' },
    { 'header':'MRP_CTRL', 'tipo':'T', 'valor':'100' },
    { 'header':'LOT_SIZE_KEY', 'tipo':'T', 'valor':'' },
    { 'header':'PROCURE_TYPE', 'tipo':'T', 'valor':'F' },
    { 'header':'SLOC_PROD', 'tipo':'T', 'valor':'' },
    { 'header':'INHOUSE_PROD', 'tipo':'T', 'valor':'' },
    { 'header':'SCH_MGN_KEY', 'tipo':'T', 'valor':'' },
    { 'header':'STRGY_GROUP', 'tipo':'T', 'valor':'' },
    { 'header':'AVAIL_CHK', 'tipo':'T', 'valor':'Y2' },
    { 'header':'ALT_BOM_SEL_METH', 'tipo':'T', 'valor':'' },
    { 'header':'MRP_DEP_REQ', 'tipo':'T', 'valor':'' },
    { 'header':'PROD_SCHEDULER', 'tipo':'T', 'valor':'' },
    { 'header':'UNDER_DLV_TOL', 'tipo':'T', 'valor':'' },
    { 'header':'OVER_DLV_TOL', 'tipo':'T', 'valor':'' },
    { 'header':'VAL_CLASS', 'tipo':'T', 'valor':'E103', 'UNBW':False },
    { 'header':'PRICE_CTRL', 'tipo':'T', 'valor':'V', 'UNBW':False },
    { 'header':'PRICE_UNIT', 'tipo':'T', 'valor':'001', 'UNBW':False },
    { 'header':'PRICE_STD', 'tipo':'T', 'valor':'', 'UNBW':False },
    { 'header':'PRICE_MAV', 'tipo':'C', 'valor':'costo_kg', 'UNBW':False  },
    { 'header':'COST_W_QTY_STRUCT_IND', 'tipo':'T', 'valor':'' },
    { 'header':'DO_NOT_COST', 'tipo':'T', 'valor':'X', 'UNBW':False },
    { 'header':'MAT_ORIG_IND', 'tipo':'T', 'valor':'X', 'UNBW':False },
    { 'header':'VAR_KEY', 'tipo':'T', 'valor':'', 'UNBW':False },
    { 'header':'COST_LOT_SIZE', 'tipo':'T', 'valor':'001', 'UNBW':False },
    { 'header':'PRCTR', 'tipo':'T', 'valor':'1170', 'UNBW':False },
    { 'header':'PROD_SCHED_PROFILE', 'tipo':'T', 'valor':'', 'UNBW':False },
    { 'header':'GRP_ORIGIN', 'tipo':'T', 'valor':'MPRI', 'UNBW':False },
    { 'header':'UMA_USALI', 'tipo':'T', 'valor':'UN' },
]

DICT_ROW_32_2_ALU = [
    { 'header':'MAT_NUM', 'tipo':'C', 'valor':'cod_sap', 'desc':'Codigo SAP' },
    { 'header':'PLANT', 'tipo':'T', 'valor':'1010' },
    { 'header':'LOAD_GRP', 'tipo':'T', 'valor':'0001', 'UNBW':False },
    { 'header':'UMA_UMP', 'tipo':'T', 'valor':'' },
    { 'header':'UMA_UMPA', 'tipo':'T', 'valor':'' },
    { 'header':'MRP_TYPE', 'tipo':'T', 'valor':'ND' },
    { 'header':'MRP_CTRL', 'tipo':'T', 'valor':'PPT' },
    { 'header':'LOT_SIZE_KEY', 'tipo':'T', 'valor':'EX' },
    { 'header':'PROCURE_TYPE', 'tipo':'T', 'valor':'E' },
    { 'header':'SLOC_PROD', 'tipo':'T', 'valor':'1010' },
    { 'header':'INHOUSE_PROD', 'tipo':'T', 'valor':'7' },
    { 'header':'SCH_MGN_KEY', 'tipo':'T', 'valor':'000' },
    { 'header':'STRGY_GROUP', 'tipo':'T', 'valor':'Z7' },
    { 'header':'AVAIL_CHK', 'tipo':'T', 'valor':'02' },
    { 'header':'ALT_BOM_SEL_METH', 'tipo':'T', 'valor':'2' },
    { 'header':'MRP_DEP_REQ', 'tipo':'T', 'valor':'1' },
    { 'header':'PROD_SCHEDULER', 'tipo':'C', 'valor':'prod_scheduler' },
    { 'header':'UNDER_DLV_TOL', 'tipo':'T', 'valor':'5' },
    { 'header':'OVER_DLV_TOL', 'tipo':'T', 'valor':'6' },
    { 'header':'VAL_CLASS', 'tipo':'T', 'valor':'T102', 'UNBW':False },
    { 'header':'PRICE_CTRL', 'tipo':'T', 'valor':'S', 'UNBW':False },
    { 'header':'PRICE_UNIT', 'tipo':'T', 'valor':'1', 'UNBW':False },
    { 'header':'PRICE_STD', 'tipo':'T', 'valor':'1' },
    { 'header':'PRICE_MAV', 'tipo':'C', 'valor':'costo_kg', 'UNBW':False  },
    { 'header':'COST_W_QTY_STRUCT_IND', 'tipo':'T', 'valor':'X' },
    { 'header':'DO_NOT_COST', 'tipo':'T', 'valor':'X', 'UNBW':False },
    { 'header':'MAT_ORIG_IND', 'tipo':'T', 'valor':'X', 'UNBW':False },
    { 'header':'VAR_KEY', 'tipo':'T', 'valor':'000001', 'UNBW':False },
    { 'header':'COST_LOT_SIZE', 'tipo':'T', 'valor':'1000', 'UNBW':False },
    { 'header':'PRCTR', 'tipo':'T', 'valor':'1020', 'UNBW':False },
    { 'header':'PROD_SCHED_PROFILE', 'tipo':'T', 'valor':'000002', 'UNBW':False },
    { 'header':'GRP_ORIGIN', 'tipo':'T', 'valor':'TERM', 'UNBW':False },
    { 'header':'UMA_USALI', 'tipo':'T', 'valor':'' },
]

def get_row_32_2_ES(sap_alum,centro=None,centro_benef=None):
    return get_row_from_dicts(DICT_ROW_32_2_ES,sap_alum)

def get_row_32_2_ALU(sap_alum,centro=None,centro_benef=None):
    return get_row_from_dicts(DICT_ROW_32_2_ALU,sap_alum)

def get_rows_32_2(sap_alum):
    rows = []
    rows.append(get_row_32_2_ES(sap_alum))
    if sap_alum.tipo_mat == 'FERT':
        rows.append(get_row_32_2_ALU(sap_alum))
    #rows.append(get_row_32_2(sap_alum,centro='1110',centro_benef=''))
    #if sap_alum.tipo_mat != 'HALB':
    #    rows.append(get_row_32_2(sap_alum,centro='1010',centro_benef=''))
    return rows

DICT_ROW_32_3 = [
    { 'header':'MAT_NUM', 'tipo':'C', 'valor':'cod_sap', 'desc':'Codigo SAP' },
    { 'header':'PLANT', 'tipo':'P', 'valor':'centro' },
    { 'header':'SLOC', 'tipo':'P', 'valor':'almacen' },
]

def get_rows_32_3(sap_alum):
    return [
        get_row_from_dicts(DICT_ROW_32_3,sap_alum,centro='1100',almacen='1130'),
        get_row_from_dicts(DICT_ROW_32_3,sap_alum,centro='1010',almacen='1010'),
        ]

DICT_ROW_32_4_ES = [
    { 'header':'MAT_NUM', 'tipo':'C', 'valor':'cod_sap', 'desc':'Codigo SAP' },
    { 'header':'SLS_ORG', 'tipo':'T', 'valor':'1100' },
    { 'header':'DIST_CH', 'tipo':'T', 'valor':'10' },
    { 'header':'SLS_UOM', 'tipo':'T', 'valor':'UN' },
    { 'header':'MAT_STAT_GRP', 'tipo':'T', 'valor':'1' },
    { 'header':'MAT_PRICE_GRP', 'tipo':'T', 'valor':'' },
    { 'header':'SLS_ITM_CAT_GRP', 'tipo':'T', 'valor':'NORM' },
    { 'header':'SLS_ACCT_ASSN_GRP', 'tipo':'T', 'valor':'30' },
    { 'header':'DELV_PLANT', 'tipo':'T', 'valor':'1100' },
    { 'header':'TAX_DEP_COUNTRY', 'tipo':'T', 'valor':'CO' },
    { 'header':'TAX_CAT', 'tipo':'T', 'valor':'MWST' },
    { 'header':'TAX_CLASS', 'tipo':'T', 'valor':'1' },
]

DICT_ROW_32_4_ALU = [
    { 'header':'MAT_NUM', 'tipo':'C', 'valor':'cod_sap', 'desc':'Codigo SAP' },
    { 'header':'SLS_ORG', 'tipo':'T', 'valor':'1050' },
    { 'header':'DIST_CH', 'tipo':'T', 'valor':'10' },
    { 'header':'SLS_UOM', 'tipo':'T', 'valor':'' },
    { 'header':'MAT_STAT_GRP', 'tipo':'T', 'valor':'1' },
    { 'header':'MAT_PRICE_GRP', 'tipo':'C', 'valor':'grupo_mat' },
    { 'header':'SLS_ITM_CAT_GRP', 'tipo':'T', 'valor':'NORM' },
    { 'header':'SLS_ACCT_ASSN_GRP', 'tipo':'T', 'valor':'30' },
    { 'header':'DELV_PLANT', 'tipo':'T', 'valor':'1010' },
    { 'header':'TAX_DEP_COUNTRY', 'tipo':'T', 'valor':'CO' },
    { 'header':'TAX_CAT', 'tipo':'T', 'valor':'MWST' },
    { 'header':'TAX_CLASS', 'tipo':'T', 'valor':'1' },
]

def get_rows_32_4(sap_alum):
    rows = []
    if sap_alum.tipo_mat == 'FERT':
        rows.append(get_row_from_dicts(DICT_ROW_32_4_ES,sap_alum))
        rows.append(get_row_from_dicts(DICT_ROW_32_4_ALU,sap_alum))
    return rows

DICT_ROW_32_5 = [
    { 'header':'MAT_NUM', 'tipo':'C', 'valor':'cod_sap', 'desc':'Codigo SAP' },
    { 'header':'WHSE_NUM', 'tipo':'T', 'valor':'CAE' },
    { 'header':'STO_TYPE', 'tipo':'P', 'valor':'bodega' },
    { 'header':'UM_WM', 'tipo':'T', 'valor':'UN' },
    { 'header':'STK_REMOVAL', 'tipo':'T', 'valor':'002' },
    { 'header':'STK_PLACEMENT', 'tipo':'T', 'valor':'002' },
    { 'header':'STO_SEC_IND', 'tipo':'P', 'valor':'sec_ind' },
]

def get_rows_32_5(sap_alum):
    rows = []
    if sap_alum.tipo_mat == 'FERT':
        rows.append(get_row_from_dicts(DICT_ROW_32_5,sap_alum,bodega='AE1',sec_ind='001'))
        rows.append(get_row_from_dicts(DICT_ROW_32_5,sap_alum,bodega='AE2',sec_ind='001'))
    elif sap_alum.tipo_mat == 'UNBW':
        rows.append(get_row_from_dicts(DICT_ROW_32_5,sap_alum,bodega='AE1',sec_ind='002'))
        rows.append(get_row_from_dicts(DICT_ROW_32_5,sap_alum,bodega='AE2',sec_ind='002'))
    return rows

DICT_ROW_32_6 = [
    { 'header':'MAT_NUM', 'tipo':'C', 'valor':'cod_sap', 'desc':'Codigo SAP' },
    { 'header':'CLASS_TYPE', 'tipo':'T', 'valor':'001' },
    { 'header':'CLASS_NAME', 'tipo':'T', 'valor':'ZMM_PERFILES' },
    { 'header':'CHARACT_NAME', 'tipo':'P', 'valor':'variable' },
    { 'header':'CHARACT_VALUE', 'tipo':'P', 'valor':'valor' },
]

def get_rows_32_6(sap_alum):
    rows = []
    rows.append(get_row_from_dicts(DICT_ROW_32_6,sap_alum,variable='ZMM_REFERENCIA',valor=sap_alum.referencia))
    rows.append(get_row_from_dicts(DICT_ROW_32_6,sap_alum,variable='ZMM_ACABADO',valor=sap_alum.cod_epics_acabado))
    rows.append(get_row_from_dicts(DICT_ROW_32_6,sap_alum,variable='ZMM_ALEACION',valor=sap_alum.aleacion))
    rows.append(get_row_from_dicts(DICT_ROW_32_6,sap_alum,variable='ZMM_TEMPLE',valor=sap_alum.temple))
    rows.append(get_row_from_dicts(DICT_ROW_32_6,sap_alum,variable='ZMM_LONGITUD',valor=sap_alum.largo_mm))
    
    return rows

DICT_ROW_32_A = [
    { 'header':'MAT_NUM', 'tipo':'C', 'valor':'cod_sap', 'desc':'Codigo SAP' },
    { 'header':'DENOM', 'tipo':'T', 'valor':'1000' },
    { 'header':'ALT_UOM', 'tipo':'T', 'valor':'UN' },
    { 'header':'NUMER', 'tipo':'C', 'valor':'peso_lineal_1000' },
]

def get_rows_32_A(sap_alum):
    rows = []
    rows.append(get_row_from_dicts(DICT_ROW_32_A,sap_alum))
    return rows

DICT_ROW_BOM_PP = [
    { 'header':'MATNR', 'tipo':'C', 'valor':'cod_sap', 'desc':'Codigo SAP' },
    { 'header':'WERKS', 'tipo':'P', 'valor':'centro', 'desc':'Codigo Centro' },
    { 'header':'STLAN', 'tipo':'T', 'valor':'1', 'desc':'Utilizacion' },
    { 'header':'STLAL', 'tipo':'P', 'valor':'alt_lista', 'desc':'Alternativa de la Lista' },
    { 'header':'DATUV', 'tipo':'P', 'valor':'fecha_dia', 'desc':'Validez' },
    { 'header':'BMENG', 'tipo':'C', 'valor':'peso_kg_str', 'desc':'Cantidad Base' },
    { 'header':'BMEIN', 'tipo':'T', 'valor':'KG', 'desc':'Unidad Base' },
    { 'header':'ZTEXT', 'tipo':'C', 'valor':'texto_lista', 'desc':'Texto de la Lista de Mat' },
    { 'header':'STKTX', 'tipo':'P', 'valor':'texto_alt_lista', 'desc':'Texto de la alternativa de Lista Mat' },
    { 'header':'POSNR', 'tipo':'P', 'valor':'num_pos', 'desc':'# de Posicion de Lista Mat' },
    #{ 'header':'POSTP', 'tipo':'P', 'valor':'cons_pos', 'desc':'Tipo de Posicion' },
    { 'header':'POSTP', 'tipo':'T', 'valor':'L', 'desc':'' },
    { 'header':'IDNRK', 'tipo':'P', 'valor':'cod_comp', 'desc':'Codigo de Componente' },
    { 'header':'KTEXT', 'tipo':'T', 'valor':'', 'desc':'Descripcion del Componente' },
    { 'header':'MENGE', 'tipo':'P', 'valor':'cant_comp', 'desc':'Cantidad de Componente' },
    { 'header':'MEINS', 'tipo':'P', 'valor':'uni_comp', 'desc':'UnidadMedida Componente' },
    { 'header':'FMENG', 'tipo':'T', 'valor':'', 'desc':'Cantidad Fija' },
    { 'header':'AUSCH', 'tipo':'T', 'valor':'', 'desc':'Rechazo Componente %' },
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

def get_row_bom_pp(sap_alum,centro,alt_lista,fecha_dia,texto_alt_lista,num_pos,cod_comp,cant_comp,uni_comp,rech_comp,almacen):
    # Genero Row Aluminio
    return get_row_from_dicts(
        DICT_ROW_BOM_PP,
        sap_alum,
        centro=centro,
        alt_lista=alt_lista,
        fecha_dia=fecha_dia,
        texto_alt_lista=texto_alt_lista,
        num_pos=num_pos,
        cod_comp=cod_comp,
        cant_comp=cant_comp,
        uni_comp=uni_comp,
        rech_comp=rech_comp,
        almacen=almacen,
        )

def rfloat_str(val):
    return str(round(float(val),3)).replace('.',',')

def float_str(val):
    return str(val).replace('.',',')

def get_rows_bom_pp_alt(sap_alum, alt_lista, texto_alt_lista, cod_alum_sap_mat):
    rows = []
    fdia = fecha_dia()
    cod_comp = cod_alum_sap_mat
    cant_comp = rfloat_str(sap_alum.peso_kg + (sap_alum.peso_kg * 0.2089))
    rows.append(get_row_bom_pp(sap_alum,centro='1010',alt_lista=alt_lista,texto_alt_lista=texto_alt_lista,fecha_dia=fdia,num_pos='0010',cod_comp=cod_comp,cant_comp=cant_comp,uni_comp='KG',rech_comp='',almacen='1050'))
    cod_comp = SCRAP_COD_SAP_MAT
    cant_comp = rfloat_str(sap_alum.peso_kg * -0.2089)
    rows.append(get_row_bom_pp(sap_alum,centro='1010',alt_lista=alt_lista,texto_alt_lista=texto_alt_lista,fecha_dia=fdia,num_pos='0020',cod_comp=cod_comp,cant_comp=cant_comp,uni_comp='KG',rech_comp='',almacen='1050'))
    cod_comp = sap_alum.cod_acabado
    cant_comp = float_str(sap_alum.cant_acabado)
    if sap_alum.pintado: rows.append(get_row_bom_pp(sap_alum,centro='1010',alt_lista=alt_lista,texto_alt_lista=texto_alt_lista,fecha_dia=fdia,num_pos='0030',cod_comp=cod_comp,cant_comp=cant_comp,uni_comp='GLN',rech_comp='',almacen='1040'))
    cod_comp = sap_alum.cod_primer
    cant_comp = float_str(sap_alum.cant_primer)
    if sap_alum.primer: rows.append(get_row_bom_pp(sap_alum,centro='1010',alt_lista=alt_lista,texto_alt_lista=texto_alt_lista,fecha_dia=fdia,num_pos='0040',cod_comp=cod_comp,cant_comp=cant_comp,uni_comp='GLN',rech_comp='',almacen='1040'))
    cod_comp = sap_alum.cod_dclear
    cant_comp = float_str(sap_alum.cant_dclear)
    if sap_alum.d_clear: rows.append(get_row_bom_pp(sap_alum,centro='1010',alt_lista=alt_lista,texto_alt_lista=texto_alt_lista,fecha_dia=fdia,num_pos='0050',cod_comp=cod_comp,cant_comp=cant_comp,uni_comp='GLN',rech_comp='',almacen='1040'))
    return rows

def get_rows_BOM_PP(sap_alum):
    rows = []
    if sap_alum.tipo_mat == 'FERT' and sap_alum.referencia.perim_exp is not None:
        cod_sap = sap_alum.get_cod_tocho(TIPO_NAC)
        if cod_sap is not None:
            rows_alt = get_rows_bom_pp_alt(sap_alum, alt_lista='1', texto_alt_lista='Version de Fabricacion Tocho Nacional', cod_alum_sap_mat=cod_sap)
            for row in rows_alt: rows.append(row)
        cod_sap = sap_alum.get_cod_tocho(TIPO_IMP)
        if cod_sap is not None:
            rows_alt = get_rows_bom_pp_alt(sap_alum, alt_lista='2', texto_alt_lista='Version de Fabricacion Tocho Importado', cod_alum_sap_mat=cod_sap)
            for row in rows_alt: rows.append(row)
        cod_sap = sap_alum.get_cod_tocho(TIPO_IMP)
        if cod_sap is not None:
            rows_alt = get_rows_bom_pp_alt(sap_alum, alt_lista='3', texto_alt_lista='Version de Fabricacion Tocho Chino', cod_alum_sap_mat=cod_sap)
            for row in rows_alt: rows.append(row)
    return rows
    

DICT_ROW_VFAB = [
    { 'header':'PLANT', 'tipo':'T', 'valor':'1010' },
    { 'header':'MAT_NUM', 'tipo':'C', 'valor':'cod_sap', 'desc':'Codigo SAP' },
    { 'header':'PRD_VERSN', 'tipo':'P', 'valor':'prd_ver' },
    { 'header':'NOMBRE_PRD_VERSN', 'tipo':'P', 'valor':'nom_prd_ver' },
    { 'header':'GRUPO_HR', 'tipo':'C', 'valor':'grupo_hr' },
    { 'header':'CONT_GRUP_HR', 'tipo':'T', 'valor':'1' },
    { 'header':'ALTER_BOM', 'tipo':'P', 'valor':'prd_ver' },
    { 'header':'UTILIZ_BOM', 'tipo':'T', 'valor':'1' }
]

def get_rows_VFAB(sap_alum):
    rows = []
    if sap_alum.tipo_mat == 'FERT' and sap_alum.referencia.perim_exp is not None:
        cod_sap = sap_alum.get_cod_tocho(TIPO_NAC)
        if cod_sap is not None:
            rows.append(get_row_from_dicts(DICT_ROW_VFAB, sap_alum, prd_ver='1', nom_prd_ver='Version de Fabricacion Tocho Nacional'))
        cod_sap = sap_alum.get_cod_tocho(TIPO_IMP)
        if cod_sap is not None:
            rows.append(get_row_from_dicts(DICT_ROW_VFAB, sap_alum, prd_ver='2', nom_prd_ver='Version de Fabricacion Tocho Importado'))
        cod_sap = sap_alum.get_cod_tocho(TIPO_IMP)
        if cod_sap is not None:
            rows.append(get_row_from_dicts(DICT_ROW_VFAB, sap_alum, prd_ver='3', nom_prd_ver='Version de Fabricacion Tocho Chino'))
    return rows

DICT_ROW_CDATA = [
    { 'header':'MODE', 'tipo':'T', 'valor':'C' },
    { 'header':'SAP_MAT_NUM', 'tipo':'C', 'valor':'cod_sap', 'desc':'Codigo SAP' },
    { 'header':'DESC', 'tipo':'C', 'valor':'desc' },
]

def get_rows_CDATA(sap_alum):
    return [get_row_from_dicts(DICT_ROW_CDATA,sap_alum),]

def exp_alum_mat():
    wout_1 = get_writer(ARCH_32_1)
    wout_2 = get_writer(ARCH_32_2)
    wout_3 = get_writer(ARCH_32_3)
    wout_4 = get_writer(ARCH_32_4)
    wout_5 = get_writer(ARCH_32_5)
    wout_6 = get_writer(ARCH_32_6)
    wout_A = get_writer(ARCH_32_A)
    #wout_CDATA = get_writer(ARCH_CDATA)
    wout_LISTA = get_writer(ARCH_LISTA)
    wout_BOM_PP = get_writer(ARCH_BOM_PP)
    wout_VFAB = get_writer(ARCH_VFAB)
    
    wout_1.writerow(get_headers_from_dicts(DICT_ROW_32_1))
    wout_2.writerow(get_headers_from_dicts(DICT_ROW_32_2_ES))
    wout_3.writerow(get_headers_from_dicts(DICT_ROW_32_3))
    wout_4.writerow(get_headers_from_dicts(DICT_ROW_32_4_ES))
    wout_5.writerow(get_headers_from_dicts(DICT_ROW_32_5))
    wout_6.writerow(get_headers_from_dicts(DICT_ROW_32_6))
    wout_A.writerow(get_headers_from_dicts(DICT_ROW_32_A))
    #wout_CDATA.writerow(get_headers_from_dicts(DICT_ROW_CDATA))
    #wout_LISTA.writerow()
    
    cod_fert = SapAluminio.objects.next_cod_fert()
    cod_unbw = SapAluminio.objects.next_cod_unbw()
    
    for s_alum in SapAluminio.objects.select_related(depth=3).filter(cargado=False):
        if s_alum.cod_sap is None:
            if s_alum.tipo_mat == 'FERT':
                s_alum.cod_sap = zfill(cod_fert,18)
                cod_fert = cod_fert + 1
            elif s_alum.tipo_mat == 'UNBW':
                s_alum.cod_sap = zfill(cod_unbw,18)
                cod_unbw = cod_unbw + 1
        
        rows_32_1 = get_rows_32_1(s_alum)
        rows_32_2 = get_rows_32_2(s_alum)
        rows_32_3 = get_rows_32_3(s_alum)
        rows_32_4 = get_rows_32_4(s_alum)
        rows_32_5 = get_rows_32_5(s_alum)
        rows_32_6 = get_rows_32_6(s_alum)
        rows_32_A = get_rows_32_A(s_alum)
        #rows_CDATA = get_rows_CDATA(s_alum)
        rows_LISTA = [s_alum.row_lista(),]
        rows_BOM_PP = get_rows_BOM_PP(s_alum)
        rows_VFAB = get_rows_VFAB(s_alum)
        
        wout_1.writerows(rows_32_1)
        wout_2.writerows(rows_32_2)
        wout_3.writerows(rows_32_3)
        wout_4.writerows(rows_32_4)
        wout_5.writerows(rows_32_5)
        wout_6.writerows(rows_32_6)
        wout_A.writerows(rows_32_A)
        #wout_CDATA.writerows(rows_CDATA)
        wout_LISTA.writerows(rows_LISTA)
        wout_BOM_PP.writerows(rows_BOM_PP)
        wout_VFAB.writerows(rows_VFAB)

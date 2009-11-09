#!/usr/bin/env python

import csv
import math
import os

DELIM = '\t'
LTERM = '\n'

ROW_C = [
    [1, 'T'],   # Tipo Registro
    [10, 'T'],  # Cliente / Solicitante
    [8, 'F'],   # Fecha Cotizacion
    [4, 'T'],   # Org Ventas
    [2, 'T'],   # Canal Distribucion
    [2, 'T'],   # Sector
    [4, 'T'],   # Clase Oferta
    [5, 'T'],   # Moneda
    [35, 'T'],  # Proyecto
    [8, 'F'],   # Valido Hasta
]

ROW_T = [
    [1, 'T'],   # Tipo Registro
    [6, 'T'],   # Posicion
    [132, 'T'], # Texto
]

ROW_P = [
    [1, 'T'],       # Tipo Registro
    [6, 'N'],       # Posicion
    [18, 'T'],      # Material
    [[13,3], 'D'],    # Cantidad
    [3, 'T'],       # Unidad Medida
    [40, 'T'],      # Texto Posicion
    [[15, 3], 'D'],    # Importe
]

ROW_V = [
    [1, 'T'],      # Tipo Registro
    [6, 'N'],      # Posicion
    [40, 'T'],     # Caracteristica
    [40, 'T'],     # Valor
]

ROW_X = [
    [1, 'T'],      # Tipo Registro
    [6, 'N'],      # Posicion
    [4, 'T'],     # Clase condicion
    [[15, 3], 'D'],     # Importe
]

ROW_B = [
    [1, 'T'],       # Tipo Registro
    [6, 'N'],       # Posicion
    [18, 'T'],      # Material
    [[13, 3], 'D'], # Cantidad
    [3, 'T'],       # Unidad Medida
    [40, 'T'],      # Texto Posicion
    [[15, 3], 'D'], # Importe
]

def fillv(valor, tipo, long):
    if tipo == 'T':
        return valor.ljust(long)
    if tipo == 'N':
        return valor.zfill(long)
    if tipo == 'F':
        return valor.strip('/\-_.').ljust(long)
    if tipo == 'D':
        declong = long[1]
        numlong = long[0]
        if valor.count('.') > 0:
            num,sep,dec = valor.rpartition('.')    
        else:
            num,sep,dec = (valor,'.','0')
        return ''.join([ num.zfill(numlong),sep,dec.ljust(declong,'0') ])

def conv_row(row,PRMS):
    wrow = [ ]
    for i in range(len(PRMS)):
        #print 'Row=%s' % row[i]
        #print 'Long=%i Tipo=%s' % (PRMS[i][0],PRMS[i][1])
        val = fillv(row[i], PRMS[i][1], PRMS[i][0])
        #print 'ValorConv=%s' % val
        wrow.append(val)
    return wrow

def conv_c(row):
    return conv_row(row,ROW_C)
    
def conv_t(row):
    return conv_row(row,ROW_T)

def conv_p(row):
    return conv_row(row,ROW_P)

def conv_b(row):
    return conv_row(row,ROW_B)
    
def conv_v(row):
    return conv_row(row,ROW_V)

def conv_x(row):
    return conv_row(row,ROW_X)

COT_TIPOS_ROWS = {
    'C' : conv_c,
    'T' : conv_t,
    'P' : conv_p,
    'B' : conv_b,
    'V' : conv_v,
    'X' : conv_x,
}

def conv_fcot(orig='TestCot.csv',dest='Test.txt'):
    rarch = os.path.join(orig)
    warch = os.path.join(dest)
    reader = csv.reader(open(rarch, 'U'), dialect='excel')
    writer = open(warch,'w')
    for row in reader:
        wrow = COT_TIPOS_ROWS[row[0]](row)
        writer.write( ''.join(wrow) + '\n')
    
    
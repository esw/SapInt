from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_unicode, smart_str
from models import Conversion, UnidadMedida, SistemaMedida, UnidadTipoSistema
from decimal import Decimal, DecimalException, localcontext, getcontext, BasicContext, DefaultContext
import re
from exceptions import *
from math import *

DefaultContext.prec = 8

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a

frac_re = re.compile('^(((?P<int>\d+))??\s*(?P<frac>(?P<num>\d+)\s*/\s*(?P<den>\d+))?)$')

def frac_format(value):
    import math
    ent = int(value)
    dec = value - Decimal(ent)
    sign, digits, exp = dec.as_tuple()
    num = int(''.join(map(str,digits)))
    den = 10 ** -exp
    g = gcd(num,den)
    num = num // g
    den = den // g
    if not ent == 0:
        if num == 0: return "%s" % ent
        else: return "%s %s/%s" %(ent,num,den)
    else:
        return "%s/%s" %(num,den)




def frac_format2(value):
    evalue=int(value)
    nvalue= int(float(value * 1000) % 1000)
    nvalue= (nvalue * 16) / 1000
    if int(nvalue > 0 ):
        dvalue=16
        x=gcd(nvalue,dvalue)
        if x > 1:
            nvalue= int(nvalue / x)
            dvalue= int(dvalue / x)
    else:
        dvalue=1
    if nvalue==0:
        return u'%s' % (nvalue)
    else:
        if evalue==0:
            return u'%s/%s' % (nvalue, dvalue)
        else:
            return u'%s %s/%s' % (nvalue, nvalue, dvalue)
    








def frac_conv_decimal(value):
    value_m = frac_re.match(value)
    if value_m:
        valor = Decimal('0')
        if value_m.group('int'): valor = Decimal(value_m.group('int'))
        if value_m.group('frac'): valor = valor + (Decimal(value_m.group('num'))/Decimal(value_m.group('den')))
        value = str(valor)
    value = smart_str(value).strip()
    return Decimal(value)

SISTEMA_FRAC = {
    'i': True,
    'm': False,
}

def frac_format_sistema(sistema):
    return SISTEMA_FRAC[sistema.ref]

class Medida(object):
    def __init__(self, valor, unidad):
        self.valor = valor
        self.unidad = unidad
    
    @property
    def tipo(self):
        return self.unidad.tipo
    
    @property
    def sistema(self):
        return self.unidad.sistema
    
    def get_valor(self,unidad=None):
        if not unidad: return self.valor
        if isinstance(unidad,str): u = UnidadMedida.buscar(unidad)
        else: u = unidad
        if not u or u == self.unidad: return self.valor
        if isinstance(u,UnidadMedida) and u != self.unidad:
            return self.valor * Conversion.buscar_factor(self.unidad,u)
        return None
    
    def _get_valor(self):
        return self._valor
    def _set_valor(self,value):
        if isinstance(value,Decimal):
            self._valor = value
        elif isinstance(value,(int,long)):
            self._valor = Decimal(str(value))
        elif isinstance(value,str):
            if value == '': self._valor=Decimal(0)
            else: self._valor = frac_conv_decimal(value)
        elif isinstance(value,float):
            pass
        else:
            self._valor=Decimal(0)
    valor = property(_get_valor,_set_valor)
    
    def _get_unidad(self):
        return self._unidad
    def _set_unidad(self,value):
        if isinstance(value,UnidadMedida):
            self._unidad = value
        elif isinstance(value,str):
            self.unidad = UnidadMedida.buscar(value)
        else:
            raise UnidadMedidaNoExiste(value)
    unidad = property(_get_unidad,_set_unidad)
    
    def to_decimal(self):
        valor = self.valor
        if isinstance(valor,Decimal):
            return valor
        elif isinstance(valor,(int,long)):
            valor = Decimal(str(valor))
        elif isinstance(valor,str):
            if value == '': valor=Decimal(0)
            else: valor = frac_conv_decimal(valor)
        elif isinstance(valor,float):
            valor = Decimal(str(valor))
        else:
            valor=Decimal(0)
        return valor
    
    def u(self,unidad=None):
        return self.get_valor(unidad)
    
    def conv_u(self,unidad):
        u = unidad
        if isinstance(unidad,str): u = UnidadMedida.buscar(unidad)
        if (self.unidad != u):
            self.valor = self.u(u)
            self.unidad = u
    
    def conv_s(self,sistema):
        if self.sistema != sistema:
            u = sistema.u_tipo(self.tipo)
            self.valor = self.u(u)
            self.unidad = u
    
    def get_unicode_u(self,unidad):
        valor = self.get_valor(unidad=unidad)
        if frac_format_sistema(unidad.sistema):
            valor = frac_format(valor)
        return u'%s (%s)' % (valor,unidad)
    
    def get_unicode_s(self,sistema):
        u_tipo = sistema.u_tipo(self.unidad.tipo)
        return self.get_unicode_u(u_tipo)
    
    def get_unicode(self,unidad=None):
        if not unidad:
            return u'%s (%s)' % (self.valor,self.unidad)
        else: return self.get_unicode_u(unidad=unidad)
    
    def get_unicode_valor(self,unidad=None):
        if not unidad or unidad==self.unidad:
            if frac_format_sistema(self.unidad.sistema):
                return frac_format(self.valor)
            return u'%s' % (self.valor)
        else:
            if not frac_format_sistema(self.unidad.sistema):
                return self.get_valor(unidad=unidad)
            else:
                return frac_format(self.get_valor(unidad=unidad))
    
    def __str__(self):
        return '%s' % (self.valor)
    
    def __unicode__(self):
        return '%s (%s)' % (self.valor,self.unidad)
    
    def __cmp__(self, other):
        if isinstance(other,Medida):
            return cmp(self.valor,other.get_valor(self.unidad))
        else:
            return NotImplemented
    
    def __add__(self, other):
        if not isinstance(other,Medida):
            raise TypeError('Tiene que sumarse con otra Medida')
        elif self.tipo != other.tipo:
            raise TipoNoCompatible(self.tipo,other.tipo)
        return Medida(self.valor+other.u(self.unidad),self.unidad)
    
    def __iadd__(self, other):
        if not isinstance(other,Medida):
            raise TypeError('Tiene que sumarse con otra Medida')
        elif self.tipo != other.tipo:
            raise TipoNoCompatible(self.tipo,other.tipo)
        self.valor += other.u(self.unidad)
        return self
    
    def __sub__(self, other):
        if not isinstance(other,Medida):
            raise TypeError('Tiene que restarse con otra Medida')
        elif self.tipo != other.tipo:
            raise TipoNoCompatible(self.tipo,other.tipo)
        return Medida(self.valor-other.u(self.unidad),self.unidad)
    
    def __isub__(self, other):
        if not isinstance(other,Medida):
            raise TypeError('Tiene que restarse con otra Medida')
        elif self.tipo != other.tipo:
            raise TipoNoCompatible(self.tipo,other.tipo)
        self.valor -= other.u(self.unidad)
        return self
    
    def __nonzero__(self):
        return bool(self.valor)

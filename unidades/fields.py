from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_unicode, smart_str
from django.db import models
from django.db import connection
from django import forms
from django.forms.util import ValidationError
from models import *
from medida import Medida
import re
from decimal import Decimal, DecimalException
from unidades.medida import frac_format, frac_format_sistema, frac_re, frac_conv_decimal

__all__ = [
    "DimensionWidget",
    "MedidaWidget",
    "DimensionFormField",
    "MedidaFormField",
    "MedidaModelField",
]

class DimensionWidget(forms.widgets.TextInput):
    pass
    #def render(self, name, value, attrs=None):
    #    if value is None: value = ''
    #    if value != '':
    #        # Only add the 'value' attribute if a value is non-empty.
    #        n_value = frac_format(value)
    #    #return mark_safe(u'<input%s />' % flatatt(final_attrs))
    #    return super(DimensionWidget,self).render(name,n_value,attrs)

class MedidaWidget(forms.widgets.MultiWidget):
    def __init__(self, attrs=None, choices=()):
        widgets = (DimensionWidget(attrs={'size':'10', 'class':'inputText'}), forms.widgets.Select(attrs=attrs,choices=choices))
        super(MedidaWidget, self).__init__(widgets, attrs)
        self.choices = choices

    def _get_choices(self):
        return self._choices

    def _set_choices(self,value):
        self._choices = value
        self.widgets[1].choices = self._choices 
    
    choices = property(_get_choices,_set_choices)

    def decompress(self, value):
        if value:
            valor = value.valor
            if frac_format_sistema(value.unidad.sistema): valor = frac_format(valor)
            return [valor, value.unidad.id]
        return [None, None]

EMPTY_VALUES = (None, '', Decimal(0))

class DimensionFormField(forms.fields.DecimalField):
    default_error_messages = {
        'zero_value': _(u'El valor no puede ser cero'),
    }
    def __init__(self,max_digits=20,decimal_places=5,*args,**kwargs):
        kwargs['max_digits'] = max_digits
        kwargs['decimal_places'] = decimal_places
        super(DimensionFormField,self).__init__(self,*args,**kwargs)
    def clean(self, value):
        """
        Validates that the input is a decimal number. Returns a Decimal
        instance. Returns None for empty values. Ensures that there are no more
        than max_digits in the number, and no more than decimal_places digits
        after the decimal point.
        """
        try:
            value = frac_conv_decimal(value)
        except DecimalException:
            raise ValidationError(self.error_messages['invalid'])
        if not self.required and value in EMPTY_VALUES:
            return None
        sign, digittuple, exponent = value.as_tuple()
        decimals = abs(exponent)
        # digittuple doesn't include any leading zeros.
        digits = len(digittuple)
        if decimals > digits:
            # We have leading zeros up to or past the decimal point.  Count
            # everything past the decimal point as a digit.  We do not count 
            # 0 before the decimal point as a digit since that would mean 
            # we would not allow max_digits = decimal_places.
            digits = decimals
        whole_digits = digits - decimals
        if self.max_digits is not None and digits > self.max_digits:
            raise ValidationError(self.error_messages['max_digits'] % self.max_digits)
        if self.decimal_places is not None and decimals > self.decimal_places:
            raise ValidationError(self.error_messages['max_decimal_places'] % self.decimal_places)
        if self.max_digits is not None and self.decimal_places is not None and whole_digits > (self.max_digits - self.decimal_places):
            raise ValidationError(self.error_messages['max_whole_digits'] % (self.max_digits - self.decimal_places))
        return value

class MedidaFormField(forms.fields.MultiValueField):
    widget = MedidaWidget
    default_error_messages = {
        'valor_invalido': _(u'Ingrese un valor valido.'),
        'unidad_invalida': _(u'Ingrese una unidad valida.'),
    }

    def __init__(self,unidades,unidad_inicial=None,*args, **kwargs):
        errors = self.default_error_messages.copy()
        if 'error_messages' in kwargs:
            errors.update(kwargs['error_messages'])
        fields = (
            DimensionFormField(error_messages={'invalid': errors['valor_invalido']},widget=DimensionWidget()),
            forms.models.ModelChoiceField(unidades,error_messages={'invalid': errors['unidad_invalida']}),
        )
        #if not initial and unidad_inicial:
        #    initial = Medida(Decimal(0),unidad_inicial)
        super(MedidaFormField, self).__init__(fields, *args, **kwargs)
        self.unidades = unidades
        
    def _set_unidades(self,value):
        self._unidades = value
        self.fields[1].query_set = value
        self.widget.choices = self.fields[1].choices
    def _get_unidades(self):
        return self._unidades
    unidades = property(_get_unidades,_set_unidades)

    def compress(self, data_list):
        if data_list:
            # Raise a validation error if time or date is empty
            # (possible if SplitDateTimeField has required=False).
            if data_list[0] in EMPTY_VALUES:
                raise ValidationError(self.error_messages['valor_invalido'])
            if data_list[1] in EMPTY_VALUES:
                raise ValidationError(self.error_messages['unidad_invalida'])
            return Medida(data_list[0],data_list[1])
        return None

class MedidaModelField(models.DecimalField):
    __metaclass__ = models.SubfieldBase
    def __init__(self,verbose_name=None, name=None, max_digits=20, decimal_places=5,unidad_alm=None,default=0, **kwargs):
        if isinstance(unidad_alm,str):
            self.str_unidad_alm = unidad_alm
        elif unidad_alm is not None:
            self.str_unidad_alm = unidad_alm.ref#UnidadMedida.buscar(unidad_alm)
        super(MedidaModelField,self).__init__(verbose_name, name, max_digits, decimal_places, **kwargs)
    @property
    def unidad_alm(self):
        return UnidadMedida.buscar(self.str_unidad_alm)
    def pre_save(self,model_instance,add):
        if self.str_unidad_alm:
            value = getattr(model_instance,self.attname)
            value.conv_u(self.unidad_alm)
            setattr(model_instance, self.attname, value)   
        #    return value
        #else:
        return super(MedidaModelField, self).pre_save(model_instance, add)
    def value_to_string(self,obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)
    def to_python(self,value):
        if isinstance(value,Medida):
            return value
        return Medida(super(MedidaModelField,self).to_python(value),self.unidad_alm)

    def to_decimal(self,value):
        return value.to_decimal()

    def get_db_prep_value(self,value):
        return connection.ops.value_to_db_decimal(self.to_decimal(value), self.max_digits, self.decimal_places)

    def get_db_prep_save(self, value):
        return connection.ops.value_to_db_decimal(self.to_decimal(value), self.max_digits, self.decimal_places)

    def formfield(self, **kwargs):
        unidades = UnidadMedida.objects.filter(tipo=self.unidad_alm.tipo)
        return MedidaFormField(unidades=unidades,**kwargs)
    